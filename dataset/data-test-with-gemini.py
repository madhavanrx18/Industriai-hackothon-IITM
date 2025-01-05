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
        return f"""Analyze the following access entry and provide a security assessment in the following JSON format:
        {{
            "risk_level": "High/Medium/Low",
            "security_concerns": "Brief description of security concerns",
            "recommended_action": "Specific action to take (Grant/Revoke/Monitor)",
            "justification": "Brief explanation of the recommendation"
        }}
        
        Consider role-based access patterns, sensitive data handling, and potential security risks:
        {all_data}
        """

    def process_batch(self, batch_df: pd.DataFrame, batch_num: int, max_retries=5) -> list:
        """Process a single batch with retry logic and return structured data."""
        prompt = self.create_batch_prompt(batch_df)
        
        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(prompt)
                try:
                    # Parse the JSON response
                    analysis = json.loads(response.text)
                    return analysis
                except json.JSONDecodeError:
                    print(f"Failed to parse JSON for batch {batch_num}. Using default values.")
                    return {
                        "risk_level": "Unknown",
                        "security_concerns": "Analysis failed",
                        "recommended_action": "Manual review required",
                        "justification": "Failed to process automatically"
                    }
            except ResourceExhausted:
                wait_time = 2 ** attempt + random.uniform(0, 1)
                print(f"Quota exceeded for batch {batch_num}. Retrying in {wait_time:.2f} seconds...")
                time.sleep(wait_time)
        
        return {
            "risk_level": "Error",
            "security_concerns": f"Failed to process batch {batch_num}",
            "recommended_action": "Manual review required",
            "justification": f"Failed after {max_retries} attempts"
        }

    def analyze_access_data(self, csv_path: str):
        """Analyzes access data in batches and saves results to a new CSV."""
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Add new columns for analysis results
        df['Risk_Level'] = ""
        df['Security_Concerns'] = ""
        df['Recommended_Action'] = ""
        df['Justification'] = ""
        
        # Calculate number of batches
        num_batches = (len(df) + self.batch_size - 1) // self.batch_size
        
        # Process each batch
        for i in range(num_batches):
            start_idx = i * self.batch_size
            end_idx = min((i + 1) * self.batch_size, len(df))
            
            print(f"Processing batch {i+1} of {num_batches}...")
            
            # Get the current batch
            batch_df = df.iloc[start_idx:end_idx].copy()
            batch_df.reset_index(drop=True, inplace=True)
            
            # Analyze batch
            analysis = self.process_batch(batch_df, i+1)
            
            # Update the main dataframe with analysis results
            df.loc[start_idx:end_idx-1, 'Risk_Level'] = analysis['risk_level']
            df.loc[start_idx:end_idx-1, 'Security_Concerns'] = analysis['security_concerns']
            df.loc[start_idx:end_idx-1, 'Recommended_Action'] = analysis['recommended_action']
            df.loc[start_idx:end_idx-1, 'Justification'] = analysis['justification']
            
            # Add small delay between batches to avoid rate limiting
            if i < num_batches - 1:
                time.sleep(2)
        
        # Save the updated DataFrame to a new CSV
        output_path = csv_path.replace('.csv', '_analyzed.csv')
        df.to_csv(output_path, index=False)
        print(f"Analysis completed. Results saved to {output_path}")

if __name__ == "__main__":
    api_key = "AIzaSyC6jA1ZAqvvUeby59CqtIJUZk148VZkMds"  # Replace with your actual API key
    analyzer = BatchAccessAnalyzer(api_key, batch_size=10)
    analyzer.analyze_access_data("user_access_data.csv")