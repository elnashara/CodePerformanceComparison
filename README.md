# Code Performance Comparison

## Introduction

The 'CodePerformanceComparison' repository is a comprehensive study that explores and compares the runtime performance of code generated with ChatGPT, an advanced language model, with that of human-produced code sourced from Stack Overflow.

The purpose of this project is to evaluate the effectiveness of AI-generated code in terms of its runtime performance. This is achieved by comparing the performance of AI-generated code with the performance of human-written code.

## Project Structure

The project is organized into several directories each serving a specific purpose:

- Root Directory: Contains the main Python files that drive the project. These files coordinate the execution of the problem set, the analysis of the runtime performance, the generation of the ChatGPT prompts, and the plotting and writing of the results.

- `stackoverflow` Directory: Contains Python scripts for different programming problems sourced from Stack Overflow. Each script represents a unique problem, and is named with a 'p' prefix followed by a number (e.g., `p1_find_missing_number.py`).

- `AutomatePromptingCodeGeneration` Directory: Contains the code for generating prompts using the ChatGPT model and the corresponding code generation. The prompts are used to guide the AI in generating the code to solve the problems.

- `data` Directory: Contains the data used for each problem in the form of CSV files. Each CSV file corresponds to a problem script in the `stackoverflow` directory.

- `results` Directory: Contains the results of executing and analyzing each problem. The results include detailed runtime information and summary statistics, and are stored as CSV files.

## File Descriptions

Here's a brief description of the key Python files in the root directory:

- `main.py`: The main entry point of the project. It orchestrates the execution of the problem set and the analysis of the runtime performance.

- `problem_set.py`: Defines the set of problems to be solved. It imports the problem modules from the `stackoverflow` directory, indicating each problem is encapsulated as a separate module.

- `runtime_performance.py`: Responsible for measuring and analyzing the runtime performance of the problem set. It uses the `runtime_execution.py` module to execute the problem set and measure its runtime.

- `chatgpt_prompt.py`: Uses the ChatGPT model to generate prompts for each problem. The prompts are used to guide the AI in generating the code to solve the problems.

- `runtime_execution.py`: Provides a mechanism for executing the problem set and measuring its runtime.

- `plot_summary_results.py`: Contains code for plotting the summary of the results, which are likely the performance results.

- `write_runtime_summary_detailed_information.py`: Writes a detailed summary of the runtime information to a CSV file.

## Requirements

This project requires Python 3.7 or higher. The Python libraries required to run this project are:

- matplotlib: Required for plotting the results.
- pandas: Required for handling and analyzing the data.
- glob: Required for handling file paths.

## Installation

To set up the project, follow these steps:

1. Clone the repository to your local machine using `git clone`.

2. Install the necessary Python libraries. If you're using pip, you can do this by running `pip install matplotlib pandas`.

## Usage

To run the project, follow these steps:

1. Navigate to the project directory.

2. Run the `main.py` script to execute the problem set and analyze their runtime performance. You can do this by running `python main.py`.

Please note that you may need to adjust these instructions based on how your project is structured and configured.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please fork the repository and make your changes, then open a pull request to the main repository. Please ensure your code adheres to the existing style for consistency.

## License

This project is licensed under the MIT License. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the condition that the above copyright notice and this permission notice are included in all copies or substantial portions of the software.

## Acknowledgements

We would like to extend our gratitude to OpenAI for providing the ChatGPT model, and to the Stack Overflow community for the programming problems used in this project.
