from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import ast
import importlib.util
import re
import importlib
import subprocess

log_file = "prompt_log.txt"

# A function to log a prompt and the output by cobining them into a dictionary and printing
# JSON that is pretty printed
def log_prompt(prompt, output):
    import json
    import pprint
    prompt_output = {"prompt":prompt, "output":output}
    with open(log_file, "a") as f:
        f.write(json.dumps(prompt_output, indent=4))
        f.write("\n\n")

def quick_prompt(msg,temperature=0):
    chat = ChatOpenAI(temperature=temperature)
    return chat([HumanMessage(content=msg)]).content


def extract_python_code(string):

    # Define the regular expression pattern to search for
    pattern = r"```[pP]ython\n(.*?)```"

    # Search for matches using the regular expression pattern
    matches = re.findall(pattern, string, re.DOTALL)

    # Return the Python code as a list
    return matches


def generate_code(system_messages, human_messages, api_key, checkfn=None, max_tries=10, prior_code=None, prior_error=None, temperature=0):
    print("Generating code...")

    chat = ChatOpenAI(temperature=temperature, openai_api_key=api_key)

    system_messages = [SystemMessage(content=message) for message in system_messages]
    human_messages = [HumanMessage(content=message) for message in human_messages]

    result = None
    code = None
    success = checkfn is None
    while not success and max_tries > 0:


        max_tries -= 1

        code_delimiter_message = """
            Any time that you generate code, the code MUST MUST MUST be enclosed in backticks with
            the name of the language that the code is written in. For example:
            
            This is python code that defines a variable with name 'a' and value 1:
            ```Python
            def a = 1
            ```
            
            """

        system_messages.insert(0, SystemMessage(content=code_delimiter_message))

        if prior_code:
            prior_code_message = """
            Your prior code was:
            ```Python
            {prior_code}
            ```
            
            """
            human_messages.append(HumanMessage(content=prior_code_message))

        if prior_error:
            fix_error_message = f"""
            
            The following error was generated when I tried to compile the code:
            
            ```Python
            {prior_error}
            ```
            Please fix the code and try again.
            
            Fixed code: 
            """
            human_messages.append(HumanMessage(content=fix_error_message))

        result = chat.generate([system_messages + human_messages])

        details = result.llm_output
        result = result.generations[0][0].text

        code = extract_python_code(result)

        if code:
            code = code[0]
            prior_code = result

            try:
                code = checkfn(code, '<string>', 'exec')
                exec(code)
            except SyntaxError as e:
                prior_error = e
                success = False
                print("Syntax Error: {}".format(e))
            except Exception as e:
                prior_error = e
                success = False
                print("Error: {}".format(e))
            else:
                print("Code executed successfully.")
                success = True


            if not success:
                print(f"Failed code: {code}")
                print(f"The code produced the error: {prior_error}")

        else:
            print(f"No code was generated in the output:\n\n\n{result}\n\n\n ")
            code = None
            prior_code = None
            prior_error = None
            success = False

        if not success:
            print(f"Trying code generation again. {max_tries} tries left")

    return {"code":code, "raw":result, "success":success, "error":prior_error}

class GeneratedModule:
    def __init__(self, raw, code, module):
        self.module = module
        self.code = code
        self.raw = raw



def install_dependencies(required_modules):
    for module in required_modules:
        try:
            importlib.import_module(module)
        except ImportError:
            print(f"{module} is not installed. Installing...")
            subprocess.run(["pip", "install", module])
        else:
            print(f"{module} is already installed.")


def extract_dependencies(code):
    tree = ast.parse(code)
    dependencies = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                dependencies.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            dependencies.add(node.module)

    return list(dependencies)

def dependency_actions_needed(code,error):

    # remove new lines
    error = str(error).replace("\n", " ")

    fix_prompt = f"""
        ERROR: The code produced the error: jinja2 must be installed to use Jinja2Templates
        ACTION: pip install jinja2
        ERROR: Traceback (most recent call last)
        ACTION: None
        ERROR: The code produced the error: fastapi must be installed to use FastAPI
        ACTION: pip install fastapi
        ERROR: Traceback (most recent call last)...
        ACTION: None
        ERROR: {error}
        ACTION: 
        """

    result = quick_prompt(fix_prompt)

    return result if "pip" in result else None


def generate_python_module(module_name, system_messages, human_messages, module_checkfn=None, max_tries=10, prior_code=None, prior_error=None, temperature=0):
    def import_module_from_string(name: str, source: str):
        spec = importlib.util.spec_from_loader(name, loader=None)
        module = importlib.util.module_from_spec(spec)
        exec(source, module.__dict__)
        return module

    def check_module(code):

        try:
            print("Installing dependencies of the generated code...")
            dependencies = extract_dependencies(code)
            install_dependencies(dependencies)
        except Exception as e:
            print(f"Failed to install dependencies: {e}")
            raise e

        print("Testing if the code is a valid Python module...")
        test_module = None
        install_tries = 10
        last_action = None

        while test_module is None and install_tries > 0:
            try:
                test_module = import_module_from_string(module_name, code)
            except Exception as e:
                install_tries = install_tries - 1
                action = dependency_actions_needed(code,e)
                if action and last_action == action:
                    break
                if action:
                    try:
                        print(f"Installing dependencies of the generated code: {action}")
                        subprocess.run(action.split(" "))
                        import site
                        from importlib import reload
                        reload(site)
                    except Exception as e:
                        last_action = action


        if not test_module:
            raise Exception("The code did not compile into a valid Python module")
        else:
            return module_checkfn(test_module)

    result = generate_code(system_messages,
                         human_messages,
                         check_module,
                         max_tries,
                         prior_code,
                         prior_error)

    code = result["code"]

    final_module = None
    if code:
        try:
            final_module = import_module_from_string(module_name, code)
        except Exception as e:
            pass

    return GeneratedModule(result, code, final_module)