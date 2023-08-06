# Import the generate_code function from ai_coder
from ai_coder import generate_code, generate_description, generate_test_case
import os
import pathlib
import configparser
import re
import csv
import time

class ChatgptAutomateprompting:
    PROMPT_ENSEMBLE = 7

    def __init__(self, api_key, problem_number, prompt_properties, filename, org_problem_name, org_problem_value):
        self.api_key = api_key
        self.problem_number = problem_number
        self.prompt_properties = prompt_properties
        self.filename = filename
        self.org_problem_name = org_problem_name
        self.org_problem_value = org_problem_value
    
    def update_python_code(self):
        data = []
        with open(self.filename, newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                time.sleep(2)
                prompt_name =  row['prompt_name']
                code_number = row['code_number']
                prompt_value = row['prompt_value']
                generated_code = row['generated_code']
                Exception = row['Exception']
                prompt_description = ''
                generated_description = ''
                prompt_test_case = ''
                generated_test_case = ''

                # if prompt_name == 'prompt_6' or prompt_name == 'prompt_7' :
                    # if int(code_number) > 62:
                try:
                    max_attempts = 3  # Set the maximum number of attempts
                    attempts = 0
                    exception = ''
                    while attempts < max_attempts:
                        try:
                            print(f'Problem Number:{self.problem_number}, Prompt Name:{prompt_name}, Prompt Number:{code_number}')
                            prompt_description,generated_description, prompt_test_case, generated_test_case = self.generate_description_test_case(prompt_value)
                            self.write_to_file(self.problem_number,prompt_name, code_number, prompt_value, generated_code, prompt_description, generated_description, prompt_test_case, generated_test_case, 'N/A')
                        except Exception as e:
                            attempts += 1
                            exception = e
                            print(f"Attempt {attempts} failed with exception: {e}")
                        else:
                            # If there is no exception, break out of the loop
                            break

                    if attempts == max_attempts:
                        print("Max attempts reached. Unable to perform the operation.")
                        self.write_to_file(self.problem_number,prompt_name, code_number, prompt_value, generated_code, prompt_description, generated_description, prompt_test_case, generated_test_case, f'Error: {str(exception)}')
                    else:
                        print("Operation was successful on attempt", attempts)
                except:
                    self.write_to_file(self.problem_number,prompt_name, code_number, prompt_value, generated_code, '', '', '', '', 'N/A')
                    continue
            
    def generate_description_test_case(self, prompt_value):
        prompt_description = f""" I'd like to generate a description of the code problem below, this should propose the method signature but not implementation, as part of the description
        {prompt_value}"""
        # generated_description = generate_description(self.api_key, [prompt_description])
        generated_description = generate_description([], [prompt_description], self.api_key, checkfn = compile, max_tries=10, temperature=0)
        prompt_test_case = f"""using the description below, I'd like to create an executable python test case with no class generated with the function name "test_funcImp" that generates some number of random inputs within a size range, sends them to a function provided to it, and then Checks if the outputs are correct.
                            {generated_description}
                            can you please create two functions , the first one named 'funcImp' and the second one named 'test_funcImp' without generating any python class and invoke test_funcImp for testing and the code combining everything into one section?"""
        generated_test_case = generate_test_case([], [prompt_test_case], self.api_key, checkfn = compile, max_tries=10, temperature=0)
        return prompt_description,generated_description, prompt_test_case, generated_test_case
    
    def generate_python_code(self):
        for prompt_number, (prompt_name, prompt_value) in enumerate(self.prompt_properties.items(), start=1):
            # if prompt_number != 8:
            #     continue

            if prompt_number == 7:
                self.generate_ensemble_python_code()
                prompt_number += 1

            prompt_value = self.get_prompt_value(prompt_value)
            for code_number in range(1, 101):
                try:
                    # Call the generate_code function with prior_code=None
                    generated_code = generate_code([], [prompt_value], self.api_key, checkfn = compile, max_tries=10, temperature=0)

                    prompt_description,generated_description, prompt_test_case, generated_test_case = self.generate_description_test_case(prompt_value)
                    self.write_to_file(self.problem_number,prompt_name, f'prompt_{prompt_number}', prompt_value, generated_code, prompt_description, generated_description, prompt_test_case, generated_test_case, 'N/A')
                except Exception as e:
                    prompt_description,generated_description, prompt_test_case, generated_test_case = self.generate_description_test_case(prompt_value)
                    self.write_to_file(self.problem_number,prompt_name, f'prompt_{prompt_number}', prompt_value, generated_code, prompt_description, generated_description, prompt_test_case, generated_test_case, f'Error: {str(e)}')
                    print (f"problem_number: {self.problem_number} - prompt_number: {str(prompt_number)} , Error: {str(e)} ")
                    continue

    def generate_ensemble_python_code(self):
        # case of prompt ensemble
        prompt_number = self.PROMPT_ENSEMBLE
        iterator = iter(self.prompt_properties.items())
        next(iterator)  # Skip the first prompt from the prompt ensemble
        
        for index, (prompt_name, prompt_value) in enumerate(iterator, start=2):
            prompt_value = self.get_prompt_value(prompt_value)
            for code_number in range(1, 21):
                try:
                    # Call the generate_code function with prior_code=None
                    generated_code = generate_code([], [prompt_value], self.api_key, checkfn = compile, max_tries=10, temperature=0)
                    prompt_description,generated_description, prompt_test_case, generated_test_case = self.generate_description_test_case(prompt_value)
                    self.write_to_file(self.problem_number,prompt_name, f'prompt_{prompt_number}', prompt_value, generated_code, prompt_description, generated_description, prompt_test_case, generated_test_case, 'N/A')
                except Exception as e:
                    prompt_description,generated_description, prompt_test_case, generated_test_case = self.generate_description_test_case(prompt_value)
                    self.write_to_file(self.problem_number,prompt_name, f'prompt_{prompt_number}', prompt_value, generated_code, prompt_description, generated_description, prompt_test_case, generated_test_case, f'Error: {str(e)}')
                    print (f"problem_number: {self.problem_number} - prompt_number: {str(prompt_number)} , Error: {str(e)} ")
                    continue

    def write_to_file(self, problem_number,prompt_name, code_number, prompt_value, generated_code, prompt_description, generated_description, prompt_test_case, generated_test_case, exception):
        directory, filename = os.path.split(self.filename)
        new_filename = f"_{filename}"
        writefile = os.path.join(directory, new_filename)
        if not os.path.isfile(writefile):
            file_mode = "w"
        else:
            file_mode = "a"
        # Write a summary information of the program's runtime to an output file.
        with open(writefile, mode=file_mode, newline='') as file:
            writer = csv.writer(file)
            if file_mode == "w":
                writer.writerow(['problem_number', 'prompt_name', 'code_number', 'prompt_value', 'generated_code', 'prompt_description', 'generated_description', 'prompt_test_case', 'generated_test_case', 'Exception'])
            writer.writerow([problem_number,prompt_name, code_number, prompt_value, generated_code, prompt_description, generated_description, prompt_test_case, generated_test_case, exception])
        
    def get_prompt_value(self, prompt_value):
        function_description = ''
        if '_arr_' in self.org_problem_name :
            function_description = config['FUNCTION_DESCRIPTION']['func_desc_arr']
            if '_one_' in self.org_problem_name:
                function_argument = config['FUNCTION_ARGUMENT']['func_one_arg_arr']
            else:
                function_argument = config['FUNCTION_ARGUMENT']['func_two_arg_arr']
            function_description = function_description.replace('<FUNCTION_ARGUMENT>',f'{function_argument}')
        if '_lnk_' in self.org_problem_name :
            function_description = config['FUNCTION_DESCRIPTION']['func_desc_lnk']
        elif '_pascal_' in self.org_problem_name :
            function_description = config['FUNCTION_DESCRIPTION']['func_desc_pascal']

        prompt_value = prompt_value.replace('<ORIGINAL_PROMPT>',f'{self.org_problem_value}').replace('<FUNCTION_DESCRIPTION>',f'{function_description}').replace("\'", "")
        return prompt_value

def clean_string(text):
    # Replace special characters with a space
    text = re.sub('[^a-zA-Z0-9\s]+', ' ', text)
    # Convert to lowercase
    text = text.lower()
    # Remove underscores and single quotes
    text = text.replace('_', '').replace("'", '')
    # Remove extra spaces
    text = re.sub('\s+', '', text).strip()
    return text

def main(config, api_key, data_dir):
    # Get the properties from the 'ORIGINAL_PROMPT' section
    original_problem_properties = config['ORIGINAL_PROBLEM']
    # Get the properties from the 'PROMPT' section
    prompt_properties = config['PROMPT']
    
    # Loop through all the properties and print their names and values
    # for org_problem_name, org_problem_value in original_problem_properties.items():
    for problem_number, (org_problem_name, org_problem_value) in enumerate(original_problem_properties.items(), start=1):
        try:
            # if problem_number == 1 or problem_number == 2:
            #     continue
            # if problem_number != 6:
            #     continue
            
            build_file_name = f"p{str(problem_number)}.{clean_string(org_problem_value)}.csv"
            print(build_file_name)

            file_name = os.path.join(data_dir, build_file_name)
            chatgpt = ChatgptAutomateprompting(api_key, problem_number, prompt_properties, file_name, org_problem_name, org_problem_value)
            chatgpt.generate_python_code()
            # chatgpt.update_python_code()
        except Exception as e:
            print (f"\t\t ++++++ Error: {str(e)} ")
            continue

def get_configuration():
    dir = os.path.dirname(__file__)
    # Create a file named 'api_key' and provide your private API key from the link provided: (https://platform.openai.com/account/api-keys)
    f = open(os.path.join(dir,"api_key"), "r")
    api_key = f.read()
    
    data_dir = pathlib.Path(dir, 'data')
    # Create a ConfigParser object
    config = configparser.ConfigParser()
    # Read the config file
    config.read(os.path.join(dir,"config.ini"))
    return config, api_key, data_dir

if __name__ == '__main__':
    config, api_key, data_dir = get_configuration()
    main(config, api_key, data_dir)
