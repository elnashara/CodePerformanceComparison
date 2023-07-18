from chatgpt_prompt import ChatGPTPrompt
from runtime_performance import RuntimePerformance
from write_runtime_summary_detailed_information import WriteRuntimeSummaryDetailedInformation
from problem_set import ProblemSet
from collections import OrderedDict
import os
import pathlib

def main():
    file_path = prompt.get_file_path(directory_path)
    if file_path is None:
        return
    content_list = prompt.get_file_content(file_path)
    
    unique_prompts = OrderedDict.fromkeys(item['prompt_name'] for item in content_list)
    print(f"total_prompts {len(unique_prompts)}")
    
    for index, content in enumerate(content_list, start=1):
        p_result_list = []
        code_segment = prompt.get_code_segment(content['generated_code'])
        print (f'index: {index}, {content["prompt_name"]}, code_number: {content["code_number"]}')
        if code_segment != 'N/A' and "Syntax error" not in code_segment:
            p_result_list = runtimeperformance.get_runtime(content["prompt_name"], content["code_number"], code_segment)
        else:
            for size in sizes:
                result = {
                    'prompt_name': content['prompt_name'],
                    'code_segment': content['generated_code'],
                    'code_index': content['code_number'],
                    'size': size,
                    'min_time': 0,
                    'avg_time': 0,
                    'max_time': 0,
                    'Exception': f'function_index: {content["prompt_name"]}, code_start_index: -1, No Python code available'
                }
                p_result_list.append(result)
        
        write.write_runtime_detailed_information(p_result_list, output_detailed)

def calculate_summary_percentage():
    write.write_runtime_summary_information(output_detailed, output_summary)
    write.calc_percentage(output_summary)

if __name__ == '__main__':
    for problem_number in range(1, 16):
        print(f'problem_number: {problem_number} ') 
        output_detailed = f"p{problem_number}_detailed_auto_execution_times.csv"
        output_summary = f"p{problem_number}_summary_auto_execution_times.csv"
        sizes = [1000, 10000, 100000]
        versions = 100
        timeout = 600 #10 min
        dir = os.path.dirname(__file__)
        directory_path = pathlib.Path(dir, 'AutomatePromptingCodeGeneration/data/')
        prefix = f"p{problem_number}."
        suffix = ".csv"

        problem_set = ProblemSet(problem_number, sizes)
        problem_info = problem_set.handle_problem_number()
        problem = problem_info[0]['problem']
        function_param = problem_info[0]['function_parameters']

        prompt = ChatGPTPrompt(problem_number, prefix, suffix)
        runtimeperformance = RuntimePerformance(problem_number, function_param, sizes, versions, timeout)
        write = WriteRuntimeSummaryDetailedInformation(problem_number, problem, dir)

        main() 
        calculate_summary_percentage()
