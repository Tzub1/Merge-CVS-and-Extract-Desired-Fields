import csv
import json

fields_to_extract = ['trial_type', 'trial_index', 'time_elapsed', 'internal_node_id', 'correct', 'rt', 'stimulus', 'response']

extracted_data = []

file_path = 'C:/Users/YiChu/OneDrive/UCD/JANATA LAB/Johnathon/csv/merged_csv.csv'

# Reading the CSV and extracting data
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['jsPsychData']:  # Checking if the jsPsychData column is not empty
            try:
                # First attempt to parse the JSON data
                trials = json.loads(row['jsPsychData'])
                # Check if further parsing is needed (if the data is doubly-encoded JSON)
                if type(trials) == str:
                    trials = json.loads(trials)
                
                # Assuming trials is now a list of dictionaries
                for trial in trials:
                    extracted_entry = {field: trial.get(field, None) for field in fields_to_extract}
                    extracted_data.append(extracted_entry)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e} - Data: {row['jsPsychData']}")
            except Exception as e:
                print(f"Other error: {e} - Data type of trials: {type(trials)}")

# Writing the extracted data to a new CSV file
with open('extracted_trials.csv', 'w', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=fields_to_extract)
    writer.writeheader()
    writer.writerows(extracted_data)

