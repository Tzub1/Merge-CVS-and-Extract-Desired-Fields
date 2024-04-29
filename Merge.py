import csv
import glob

path = 'C:/Users/YiChu/OneDrive/UCD/JANATA LAB/Johnathon/csv/csv_data/*.csv' 
csv_files = glob.glob(path)

# Master list to hold all data
all_data = []

# Process each file
for file in csv_files:
    with open(file, mode='r', newline='') as f:
        reader = csv.reader(f)
        if not all_data:
            # Include header only from the first file
            all_data.extend(reader)
        else:
            next(reader)  # Skip the header
            all_data.extend(reader)

# Path for the combined CSV file
output_file = 'C:/Users/YiChu/OneDrive/UCD/JANATA LAB/Johnathon/csv/merged_csv.csv'

# Write all data to a new CSV file
with open(output_file, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(all_data)