import google.generativeai as genai
import pandas as pd
import json
import time
import random
from google.api_core.exceptions import ResourceExhausted

class BatchAccessAnalyzer:
    def __init__(self, api_key: str, batch_size: int = 10):
        # Initialize Gemini API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.batch_size = batch_size

    def create_batch_prompt(self, batch_df: pd.DataFrame) -> str:
        """Creates a prompt for a single batch of access data."""
        data_lines = []
        for idx, row in batch_df.iterrows():
            entry = f"""
            Entry {idx + 1}:
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

    def process_batch(self, batch_df: pd.DataFrame, batch_num: int, max_retries=5) -> str:
        """Process a single batch with retry logic."""
        prompt = self.create_batch_prompt(batch_df)
        
        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except ResourceExhausted:
                wait_time = 2 ** attempt + random.uniform(0, 1)
                print(f"Quota exceeded for batch {batch_num}. Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
        
        return f"Failed to process batch {batch_num} after {max_retries} attempts."

    def analyze_access_data(self, csv_path: str):
        """Analyzes access data in batches."""
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Calculate number of batches
        num_batches = (len(df) + self.batch_size - 1) // self.batch_size
        
        # Create output file
        with open("batch_analysis_report.txt", 'w') as f:
            f.write("Access Permissions Batch Analysis Report\n")
            f.write("=====================================\n\n")
            
            # Process each batch
            for i in range(num_batches):
                start_idx = i * self.batch_size
                end_idx = min((i + 1) * self.batch_size, len(df))
                batch_df = df.iloc[start_idx:end_idx].copy()
                batch_df.reset_index(drop=True, inplace=True)
                
                print(f"Processing batch {i+1} of {num_batches}...")
                
                # Analyze batch
                batch_result = self.process_batch(batch_df, i+1)
                
                # Write batch results to file
                f.write(f"\nBatch {i+1} Analysis:\n")
                f.write("-------------------\n")
                f.write(batch_result)
                f.write("\n\n")
                
                # Add small delay between batches to avoid rate limiting
                if i < num_batches - 1:
                    time.sleep(2)
        
        print("Analysis completed. Check 'batch_analysis_report.txt' for the complete report.")

if __name__ == "__main__":
    api_key = "AIzaSyC6jA1ZAqvvUeby59CqtIJUZk148VZkMds"  # Replace with your actual API key
    analyzer = BatchAccessAnalyzer(api_key, batch_size=10)
    analyzer.analyze_access_data("user_access_data.csv")