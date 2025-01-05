import google.generativeai as genai
import pandas as pd
import json
import time
import random
from google.api_core.exceptions import ResourceExhausted

class AccessAnalyzer:
    def __init__(self, api_key: str):
        # Initialize Gemini API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def create_batch_prompt(self, df: pd.DataFrame) -> str:
        """Creates a single prompt with all access data for analysis."""
        # Convert DataFrame to formatted string
        data_lines = []
        for _, row in df.iterrows():
            entry = f"""
            Entry {_+1}:
            User: {row['User_ID']} (Role: {row['Role']})
            File: {row['File_Path']}
            Behavior Probability: {row['Behavior_Probability']}
            Current Access: {row['Access_Granted']}
            """
            data_lines.append(entry)
        all_data = "\n".join(data_lines)

        return f"""Analyze the following batch of access permissions and provide a comprehensive security assessment. 
        Consider role-based access patterns, sensitive data handling, and potential security risks:

        {all_data}

        Provide your analysis with:
        1. Overall security assessment
        2. Patterns in access permissions
        3. Potential security concerns
        4. Recommendations for access control improvements
        """

    def analyze_access_data(self, csv_path: str, max_retries=5):
        """Analyzes all access data in batch with retry logic."""
        df = pd.read_csv(csv_path)
        prompt = self.create_batch_prompt(df)

        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(prompt)
                with open("batch_analysis_report.txt", 'w') as f:
                    f.write("Access Permissions Batch Analysis Report\n")
                    f.write("=====================================\n\n")
                    f.write(response.text)
                print("Analysis completed. Check 'batch_analysis_report.txt' for the report.")
                break
            except ResourceExhausted:
                wait_time = 2 ** attempt + random.uniform(0, 1)
                print(f"Quota exceeded. Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
        else:
            print("Exceeded maximum retries. Please check your quota limits.")

if __name__ == "__main__":
    api_key = "AIzaSyC6jA1ZAqvvUeby59CqtIJUZk148VZkMds"  # Replace with your actual API key
    analyzer = AccessAnalyzer(api_key)
    analyzer.analyze_access_data("user_access_data.csv")

