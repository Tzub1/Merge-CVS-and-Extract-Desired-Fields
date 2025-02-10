import csv
import json
##import statistics

input = ''
output = 'extracted.csv'

def mean(rt_list):
    valid_rts = list(filter(None, rt_list)) # filter out None
    return sum(valid_rts) / len(valid_rts) if valid_rts else None

def correctness(correct_list):
    valid_responses = [c for c in correct_list if c is not None]
    true_count = valid_responses.count(True)
    total_count = len(valid_responses)
    return (true_count / total_count) if total_count > 0 else None

##def SD(rt_list):
##    valid_rts = list(filter(None, rt_list))


# Open the input CSV file
with open(input, 'r', encoding='UTF-8') as infile:
    reader = csv.DictReader(infile)
    
    # Prepare the output CSV file
    with open(output, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([
            'ResponseId',
            'jsPsychData_AXCPT1_rt', 'jsPsychData_AXCPT1_correctness',
            'jsPsychData_AXCPT2_rt', 'jsPsychData_AXCPT2_correctness',
            'jsPsychData_inducing_rt', 'jsPsychData_inducing_correctness'
        ])  # Writing the header
        
        # Iterate over each row in the input file
        for row in reader:
            response_id = row.get('ResponseId') 
            
            # Initialize lists to store rt and correctness values for each section
            rt_values_AXCPT1 = []
            correctness_values_AXCPT1 = []
            rt_values_AXCPT2 = []
            correctness_values_AXCPT2 = []
            rt_values_inducing = []
            correctness_values_inducing = []

            for section in ['jsPsychData_AXCPT1', 'jsPsychData_AXCPT2', 'jsPsychData_inducing']:
                for i in range(5):
                    column_name = f'{section}_{i}'
                    json_data = row.get(column_name)
                    
                    if json_data:
                        try:
                            parsed_data = json.loads(json_data)
                            for entry in parsed_data:
                                if isinstance(entry, str):
                                    entry = json.loads(entry)
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
            
            mean_rt_AXCPT1 = mean(rt_values_AXCPT1)
            correctness_AXCPT1 = correctness(correctness_values_AXCPT1)
            mean_rt_AXCPT2 = mean(rt_values_AXCPT2)
            correctness_AXCPT2 = correctness(correctness_values_AXCPT2)
            mean_rt_inducing = mean(rt_values_inducing)
            correctness_inducing = correctness(correctness_values_inducing)
            # just look at the mean is not enough, as well as how much error, and the data variation, standard deviation, to look at how their cognitive function changes over time.
            writer.writerow([
                response_id,
                mean_rt_AXCPT1, correctness_AXCPT1,
                mean_rt_AXCPT2, correctness_AXCPT2,
                mean_rt_inducing, correctness_inducing
            ])