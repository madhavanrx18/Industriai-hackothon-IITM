'''working''' 
import csv
import requests

def validate_access_with_gemini_api(access_info):
    """
    Mock function to validate `Access_Granted` using Gemini API.
    Replace this with the actual API endpoint and logic.
    """
    # Replace with actual Gemini API URL and headers if required
    api_url = "https://gemini-api.example.com/validate-access"
    response = requests.post(api_url, json=access_info)
    if response.status_code == 200:
        return response.json().get("is_access_granted", False)
    else:
        print(f"Error: Failed to validate access with status code {response.status_code}")
        return False

def process_csv(input_csv, output_csv):
    """
    Reads a CSV file line by line, validates Access_Granted, and writes updated rows to a new CSV.
    """
    with open(input_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            access_info = {
                "User_ID": row["User_ID"],
                "Role": row["Role"],
                "File_Path": row["File_Path"],
                "Access_Granted": row["Access_Granted"]
            }

            # Validate access using Gemini API
            is_access_granted = validate_access_with_gemini_api(access_info)

            # Update row with validated access
            row["Access_Granted"] = str(is_access_granted)

            # Write updated row to output CSV
            writer.writerow(row)

if __name__ == "__main__":
    input_csv_path = "dataset/user_access_data.csv"  # Input CSV file path
    output_csv_path = "output.csv"  # Output CSV file path

    process_csv(input_csv_path, output_csv_path)
    print(f"Processing complete. Updated CSV saved to {output_csv_path}.")
