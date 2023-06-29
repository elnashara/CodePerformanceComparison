# Import the generate_code function from ai_coder
from ai_coder import generate_code
import os
import pathlib
import configparser
import re
import csv

class ChatgptAutomateprompting:
    PROMPT_ENSEMBLE = 7

    def __init__(self, problem_number, prompt_properties, filename, org_problem_name, org_problem_value):
        self.problem_number = problem_number
        self.prompt_properties = prompt_properties
        self.filename = filename
        self.org_problem_name = org_problem_name
        self.org_problem_value = org_problem_value
    
    def generate_python_code(self):
        for prompt_number, (prompt_name, prompt_value) in enumerate(self.prompt_properties.items(), start=1):
            prompt_value = self.get_prompt_value(prompt_value)
            for code_number in range(1, 101):
                try:
                    # Call the generate_code function with prior_code=None
                    generated_code = generate_code([], [prompt_value], api_key, checkfn = compile, max_tries=10, temperature=0)
                    self.write_to_file(self.problem_number,prompt_name, code_number, prompt_value, generated_code, 'N/A')
                except Exception as e:
                    self.write_to_file(self.problem_number,prompt_name, code_number, prompt_value, generated_code, f'Error: {str(e)}')
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
                    generated_code = generate_code([], [prompt_value], api_key, checkfn = compile, max_tries=10, temperature=0)
                    self.write_to_file(self.problem_number,f'prompt_{prompt_number}', code_number, prompt_value, generated_code, 'N/A')
                except Exception as e:
                    self.write_to_file(self.problem_number,f'prompt_{prompt_number}', code_number, prompt_value, generated_code, f'Error: {str(e)}')
                    print (f"problem_number: {self.problem_number} - prompt_number: {str(prompt_number)} , Error: {str(e)} ")
                    continue

    def write_to_file(self, problem_number,prompt_name, code_number, prompt_value, generated_code, exception):
        if not os.path.isfile(self.filename):
            file_mode = "w"
        else:
            file_mode = "a"
        # Write a summary information of the program's runtime to an output file.
        with open(self.filename, mode=file_mode, newline='') as file:
            writer = csv.writer(file)
            if file_mode == "w":
                writer.writerow(['problem_number', 'prompt_name', 'code_number', 'prompt_value', 'generated_code', 'Exception'])
            writer.writerow([problem_number,prompt_name, code_number, prompt_value, generated_code, exception])
        
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
            if problem_number != 12:
                continue
            build_file_name = f"p{str(problem_number)}.{clean_string(org_problem_value)}.csv"
            print(build_file_name)

            file_name = os.path.join(data_dir, build_file_name)
            chatgpt = ChatgptAutomateprompting(problem_number, prompt_properties, file_name, org_problem_name, org_problem_value)
            # chatgpt.generate_python_code()
            chatgpt.generate_ensemble_python_code()
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

