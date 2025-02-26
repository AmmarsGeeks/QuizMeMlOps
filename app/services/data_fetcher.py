import requests

class TestDataFetcher:
    def __init__(self, api_url: str):
        self.api_url = api_url
        
    def get_tests(self):
        response = requests.get(f"{self.api_url}/getTests")
        response.raise_for_status()
        return response.json()['data']