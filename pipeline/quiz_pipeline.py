import requests
from app.services.data_cleaner import TestDataCleaner

def run_pipeline():
    # 1. Fetch data
    data = requests.get("https://us-central1-startquizme.cloudfunctions.net/getTests").json()['data']
    
    # 2. Clean data
    cleaned_data = TestDataCleaner.clean_test_data(data)
    
    # 3. Export data (optional)
    import pandas as pd
    pd.DataFrame(cleaned_data).to_csv("processed_tests.csv")
    
    return cleaned_data

if __name__ == "__main__":
    run_pipeline()