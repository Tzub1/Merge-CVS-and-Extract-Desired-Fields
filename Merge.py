import csv
import os

path = 'where the all csv data files are/*.csv' 

# defined empty list
all_data = []

# the list of csv files in the paht
csv_files = [file for file in os.listdir(path)]

# loop all files in the folder
for file in csv_files:
    with open(os.path.join(path, file), mode='r', newline='') as f:
        reader = csv.reader(f)
        if not all_data:
            # if the list is empty then put the header since it is the first file being processed
            all_data.extend(reader)
        else:
            next(reader)  # skip the header if it is not the first file
            all_data.extend(reader)

# path for the merged CSV file
output_file = 'C:/Users/YiChu/OneDrive/UCD/JANATA LAB/Johnathon/csv/merged_csv.csv'

#write all data to a new CSV file
with open(output_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(all_data)