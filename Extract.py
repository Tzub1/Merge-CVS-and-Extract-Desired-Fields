import csv
import json

fields_to_extract = ['trial_type', 'trial_index', 'time_elapsed', 'internal_node_id', 'correct', 'rt', 'stimulus', 'response']

extracted_data = []

file_path = 'where the merged data file is'

# Reading the CSV and extracting data
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['jsPsychData']:  # checking if the jsPsychData column is not empty
            try:
                # parse the JSON string
                trials = json.loads(row['jsPsychData'])
                # seems like the json string is double encoded
                if type(trials) == str:
                    trials = json.loads(trials)
                
                # assume trials is now a list of dictionaries
                for trial in trials:
                    extracted_entry = {field: trial.get(field, None) for field in fields_to_extract}
                    extracted_data.append(extracted_entry)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e} - Data: {row['jsPsychData']}")
            except Exception as e:
                print(f"Other error: {e} - Data type of trials: {type(trials)}")

# writing the extracted data to a new csv file
with open('extracted_trials.csv', 'w', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=fields_to_extract)
    writer.writeheader()
    writer.writerows(extracted_data)