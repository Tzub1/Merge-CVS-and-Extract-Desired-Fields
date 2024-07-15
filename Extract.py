import csv
import json

fields_to_extract = ['trial_type', 'trial_index', 'time_elapsed', 'internal_node_id', 'correct', 'rt', 'stimulus', 'response']

extracted_data = []

file_path = 'where the merged data file is'

# Reading the CSV and extracting data
with open(file_path, 'r', newline='') as csvfile:
    # create object reader --> ilterate over rows as dic (column being the key)
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['jsPsychData_testing']:  # checking if the jsPsychData column is not empty
            try:
                # decode the json string for the first time and make it a python dic
                trials = json.loads(row['jsPsychData_testing'])
                # the string in the file might be double encoded so check if it is still a string and decoded once again
                if type(trials) == str:
                    trials = json.loads(trials)
                
                # starts a loop that iterates over each trial in the trials list
                for trial in trials:
                    # creates a dictionary 'extracted' with the fields specified in fields_to_extract
                    extracted = {field: trial.get(field, None) for field in fields_to_extract}
                    extracted_data.append(extracted)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e} - Data: {row['jsPsychData_testing']}")
            except Exception as e:
                print(f"Other error: {e} - Data type of trials: {type(trials)}")

        if row['jsPsychData_inducing']:  # checking if the jsPsychData column is not empty
            try:
                # decode the json string for the first time and make it a python dic
                trials = json.loads(row['jsPsychData_inducing'])
                # the string in the file might be double encoded so check if it is still a string and decoded once again
                if type(trials) == str:
                    trials = json.loads(trials)
                
                # starts a loop that iterates over each trial in the trials list
                for trial in trials:
                    # creates a dictionary 'extracted' with the fields specified in fields_to_extract
                    extracted = {field: trial.get(field, None) for field in fields_to_extract}
                    extracted_data.append(extracted)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e} - Data: {row['jsPsychData_inducing']}")
            except Exception as e:
                print(f"Other error: {e} - Data type of trials: {type(trials)}")

        if row['jsPsychData_AXCPT1']:  # checking if the jsPsychData column is not empty
            try:
                # decode the json string for the first time and make it a python dic
                trials = json.loads(row['jsPsychData_AXCPT1'])
                # the string in the file might be double encoded so check if it is still a string and decoded once again
                if type(trials) == str:
                    trials = json.loads(trials)
                
                # starts a loop that iterates over each trial in the trials list
                for trial in trials:
                    # creates a dictionary 'extracted' with the fields specified in fields_to_extract
                    extracted = {field: trial.get(field, None) for field in fields_to_extract}
                    extracted_data.append(extracted)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e} - Data: {row['jsPsychData_AXCPT1']}")
            except Exception as e:
                print(f"Other error: {e} - Data type of trials: {type(trials)}")

        if row['jsPsychData_AXCPT2']:  # checking if the jsPsychData column is not empty
            try:
                # decode the json string for the first time and make it a python dic
                trials = json.loads(row['jsPsychData_AXCPT2'])
                # the string in the file might be double encoded so check if it is still a string and decoded once again
                if type(trials) == str:
                    trials = json.loads(trials)
                
                # starts a loop that iterates over each trial in the trials list
                for trial in trials:
                    # creates a dictionary 'extracted' with the fields specified in fields_to_extract
                    extracted = {field: trial.get(field, None) for field in fields_to_extract}
                    extracted_data.append(extracted)
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e} - Data: {row['jsPsychData_AXCPT2']}")
            except Exception as e:
                print(f"Other error: {e} - Data type of trials: {type(trials)}")

# writing the extracted data to a new csv file
with open('extracted_trials.csv', 'w', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=fields_to_extract)
    writer.writeheader()
    writer.writerows(extracted_data)