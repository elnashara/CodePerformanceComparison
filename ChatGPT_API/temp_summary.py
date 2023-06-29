from collections import defaultdict
import os
import csv
import pandas as pd

problem = 1
dir = "D:\chatGPT-humanExpert\ChatGPT_API"
output_detailed_file = f"p{problem}_detailed_auto_execution_times.csv"
output_summary_file = f"p{problem}_summary_auto_execution_times.csv"

def write_runtime_summary_information(output_detailed_file, output_summary_file):
    
    result = defaultdict(lambda: defaultdict(list))
    
    import pandas as pd
    file_loc_detailed = os.path.join(dir,'results',output_detailed_file)

    if not os.path.exists(file_loc_detailed):
        return

    data = pd.read_csv(file_loc_detailed)
    # Iterate over the rows
    for index, row in data.iterrows():
        # print(index)
        prompt_name = row.loc['prompt_name']
        size = row.loc['Size']
        min_time = row.loc['Min']
        avg_time = row.loc['Average']
        max_time = row.loc['Max']
        # ignore the python code that has an exception either infinit loop or syntax error
        if min_time == 0 or min_time >= 600:
            continue
        
        result[(prompt_name, size)]['min_time'].append(min_time)
        result[(prompt_name, size)]['avg_time'].append(avg_time)
        result[(prompt_name, size)]['max_time'].append(max_time)

    write_header = False
    file_loc_summary = os.path.join(dir,'results',output_summary_file)
    if not os.path.isfile(file_loc_summary):
        write_header = True

    # Write a summary information of the program's runtime to an output file.
    with open(file_loc_summary, mode='a', newline='') as file:
        writer = csv.writer(file)
        if write_header == True:
            writer.writerow(['Size', 'prompt_name', 'Function', 'Min', 'Average', 'Max'])
        for (prompt_name, size), times in result.items():
            print(f"Size: {size}")
            print(f"prompt Index: {prompt_name}")
            min_time = min(times['min_time'])
            avg_time = sum(times['avg_time'])/len(times['avg_time'])
            max_time = max(times['max_time'])

            print(f"Min of min_time: {min_time}")
            print(f"Avg of avg_time: {avg_time}")
            print(f"Max of max_time: {max_time}")
            print()

            writer.writerow([size,str(prompt_name), problem , min_time, avg_time, max_time])

def calc_percentage(output_summary_file):
    import pandas as pd
    try:
        # Read the data from the CSV file
        file = os.path.join(dir,'results',output_summary_file)
        if not os.path.exists(file):
            return

        df = pd.read_csv(file)
        print(file)
        # Calculate the minimum average per size
        min_avg_df = df.groupby('Size')['Average'].min().reset_index()
        min_avg_df.columns = ['Size', 'Minimum Average']
        # Merge the minimum average DataFrame with the original DataFrame
        merged_df = pd.merge(df, min_avg_df, on='Size', how='left')
        # Calculate the percentage with respect to the minimum average per size
        merged_df['Percentage'] = 100*((merged_df['Average'] - merged_df['Minimum Average']) / merged_df['Minimum Average'] if (merged_df['Minimum Average']!=0).any() else 0)
        # Save the updated result back to the CSV file
        merged_df.to_csv(file, index=False)
    except Exception as e:
        print (f"Error: {str(e)} ")

write_runtime_summary_information(output_detailed_file, output_summary_file)
calc_percentage(output_summary_file)