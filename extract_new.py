import csv
import json


# Path to the input and output files
input_file_path = 'C:/Users/YiChu/OneDrive/Desktop/Gratitude_and_data_quality-Aug5thVersion_August+21,+2024_10.07.csv'
output_file_path = 'C:/Users/YiChu/OneDrive/Desktop/extractedas.csv'

# Function to calculate the mean of a list, returning None if the list is empty
def calculate_mean(rt_list):
    valid_rts = [rt for rt in rt_list if rt is not None]  # Filter out None values
    return sum(valid_rts) / len(valid_rts) if valid_rts else None

# Function to calculate the percentage of 'true' values for correctness
def calculate_correctness(correct_list):
    true_count = correct_list.count(True)
    total_count = len(correct_list)
    return (true_count / total_count) * 100 if total_count > 0 else None

# Open the input CSV file
with open(input_file_path, mode='r', encoding='ISO-8859-1') as infile:
    reader = csv.DictReader(infile)
    
    # Prepare the output CSV file
    with open(output_file_path, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([
            'ResponseId',
            'jsPsychData_AXCPT1_rt', 'jsPsychData_AXCPT1_correctness',
            'jsPsychData_AXCPT2_rt', 'jsPsychData_AXCPT2_correctness',
            'jsPsychData_inducing_rt', 'jsPsychData_inducing_correctness'
        ])  # Writing the header
        
        # Iterate over each row in the input file
        for row in reader:
            response_id = row.get('ResponseId')  # Get the ResponseId for the current row
            
            # Initialize lists to store rt and correctness values for each section
            rt_values_AXCPT1 = []
            correctness_values_AXCPT1 = []
            rt_values_AXCPT2 = []
            correctness_values_AXCPT2 = []
            rt_values_inducing = []
            correctness_values_inducing = []
            
            # Process each section separately
            for section in ['jsPsychData_AXCPT1', 'jsPsychData_AXCPT2', 'jsPsychData_inducing']:
                for i in range(5):  # Assuming there are up to 5 numbered columns per section (adjust if needed)
                    column_name = f'{section}_{i}'
                    json_data = row.get(column_name)
                    
                    if json_data:
                        try:
                            parsed_data = json.loads(json_data)
                            for entry in parsed_data:
                                if isinstance(entry, str):
                                    entry = json.loads(entry)  # Parse if the entry is a string
                                rt_value = entry.get('rt')
                                correct_value = entry.get('correct')
                                
                                if section == 'jsPsychData_AXCPT1':
                                    rt_values_AXCPT1.append(rt_value)
                                    correctness_values_AXCPT1.append(correct_value)
                                elif section == 'jsPsychData_AXCPT2':
                                    rt_values_AXCPT2.append(rt_value)
                                    correctness_values_AXCPT2.append(correct_value)
                                elif section == 'jsPsychData_inducing':
                                    rt_values_inducing.append(rt_value)
                                    correctness_values_inducing.append(correct_value)
                        except json.JSONDecodeError:
                            # Handle JSON decoding errors
                            pass
            
            # Calculate the mean rt and correctness for each section
            mean_rt_AXCPT1 = calculate_mean(rt_values_AXCPT1)
            correctness_AXCPT1 = calculate_correctness(correctness_values_AXCPT1)
            mean_rt_AXCPT2 = calculate_mean(rt_values_AXCPT2)
            correctness_AXCPT2 = calculate_correctness(correctness_values_AXCPT2)
            mean_rt_inducing = calculate_mean(rt_values_inducing)
            correctness_inducing = calculate_correctness(correctness_values_inducing)
            
            # Write the results to the output CSV
            writer.writerow([
                response_id,
                mean_rt_AXCPT1, correctness_AXCPT1,
                mean_rt_AXCPT2, correctness_AXCPT2,
                mean_rt_inducing, correctness_inducing
            ])

print("Data extraction, mean calculation, and correctness calculation complete and saved to", output_file_path)
