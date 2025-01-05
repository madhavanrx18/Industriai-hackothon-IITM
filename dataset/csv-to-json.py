import csv
import json

def csv_to_json(csv_filename, json_filename):
    # Read CSV data
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rows = list(csv_reader)
    
    # Write JSON data
    with open(json_filename, mode='w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=4)

    print(f"CSV file '{csv_filename}' has been converted to JSON and saved as '{json_filename}'")

# Example usage
csv_filename = 'dataset/synthetic_data.csv'  # Replace with your CSV file path
json_filename = 'dataset/synthetic_data.json'  # Desired output JSON file path
csv_to_json(csv_filename, json_filename)
