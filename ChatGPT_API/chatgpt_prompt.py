import os
import ast
import csv

class ChatGPTPrompt:
    def __init__(self, problem_number, prefix, suffix):
        self.problem_number = problem_number
        self.prefix = prefix
        self.suffix = suffix
        
    def get_file_path(self, directory_path):
        # Loop through all the files in the directory
        for filename in os.listdir(directory_path):
            if filename.startswith(self.prefix) and filename.endswith(self.suffix):
                print(f"filename: {filename}")
                # Construct the full file path
                file_path = os.path.join(directory_path, filename)
                return file_path

    def get_file_content(self, file_path):
        file_content_list=[]
        try:
            with open(file_path) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    result = {
                        'problem_number': row['problem_number'],
                        'prompt_name': row['prompt_name'],
                        'code_number': row['code_number'],
                        'prompt_value': row['prompt_value'],
                        'generated_code': row['generated_code'],
                        'Exception': row['Exception']
                    }
                    file_content_list.append(result)
        except FileNotFoundError:
            print("File not found")
        except UnicodeDecodeError:
            print("Unable to decode the file with the specified encoding")

        return file_content_list

    def get_code_segment(self, generated_code):
        try:
            code_start_index = generated_code.replace("```python","```Python").find("```Python")
            if code_start_index > 0: 
                code_end_index = generated_code.find("```", code_start_index + len("```Python"))
                code_string = generated_code[code_start_index + len("```Python"):code_end_index]
                # Cleaning up the code string and replacing "\n" with actual newline character
                code_string = code_string.strip().replace("\\n", "\n")
                # Removing escape sequences
                code_string = code_string.encode().decode('unicode_escape')
                # Evaluating the code string and capturing the AST
                code_ast = ast.parse(code_string.replace("print(", "pass #print("), mode='exec')
                # Extracting the source code from the AST
                code_segment = ast.unparse(code_ast)

                return code_segment
            else:
                return 'N/A'
        except SyntaxError as e:
            error = f"Syntax error: {e}"
            print(error)
            return error
