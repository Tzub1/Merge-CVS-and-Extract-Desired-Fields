import csv
import json

fields_to_extract = ['trial_type', 'trial_index', 'time_elapsed', 'internal_node_id', 'correct', 'rt', 'stimulus', 'response']

extracted_data = []

file_path = '/mnt/data/Survey+template+test+-+test_July+14,+2024_17.48.csv'

# Define a function to process each jsPsychData column with a label and handle empty or non-JSON content
def process_jspsych_data_with_label(column_name, label, reader):
    extracted_data = []
    extracted_data.append({field: label for field in fields_to_extract})  # Add label row
    for row in reader:
        if row[column_name]:  # checking if the jsPsychData column is not empty
            try:
                # Decode the json string for the first time and make it a python dict
                trials = json.loads(row[column_name])
                # The string in the file might be double encoded so check if it is still a string and decode once again
                if type(trials) == str:
                    trials = json.loads(trials)
                
                # Loop over each trial in the trials list
                for trial in trials:
                    # Create a dictionary 'extracted' with the fields specified in fields_to_extract
                    extracted = {field: trial.get(field, None) for field in fields_to_extract}
                    extracted_data.append(extracted)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e} - Data: {row[column_name]}")
            except Exception as e:
                print(f"Other error: {e} - Data type of trials: {type(trials)}")
    return extracted_data

# Reading the CSV and extracting data from each jsPsychData column
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    extracted_data.extend(process_jspsych_data_with_label('jsPsychData_testing', 'jsPsychData_testing', reader))

with open(file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    extracted_data.extend(process_jspsych_data_with_label('jsPsychData_inducing', 'jsPsychData_inducing', reader))

with open(file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    extracted_data.extend(process_jspsych_data_with_label('jsPsychData_AXCPT1', 'jsPsychData_AXCPT1', reader))

# Writing the extracted data to a new CSV file with labels
with open('labeled_extracted_trials.csv', 'w', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=fields_to_extract)
    writer.writeheader()
    writer.writerows(extracted_data)
