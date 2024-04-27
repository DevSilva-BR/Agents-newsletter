import requests

class Test_API:
    def __init__(self):
        self.API_KEY = "c30e67be0d1540bc83050a5100daba57"
        self.base_url = "https://newsapi.org/v2/everything"
    def test_api_connection(self, api):
        query = "brasil"
        params = {
            'q': query,
            'from': '2024-04-20',
            'sortBy': 'publishedAt',
            'apiKey': api,
            'language': 'pt',
            'pageSize': 5,
        }
        response = requests.get(self.base_url, params=params)
        print(f"Test API Request URL: {response.status_code}")  # For debugging
        if response.status_code == 200:
            return f"Api valida: {response.status_code}"
        else:
            return f"Failed to fetch articles, status code: {response.status_code}, response: {response.text}"




