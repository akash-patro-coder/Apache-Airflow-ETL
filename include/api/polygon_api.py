import requests

def get_polygon_data(api_key, ticker, ds):
    url = f"https://api.polygon.io/v1/open-close/{ticker}/{ds}?adjusted=true&apiKey={api_key}"
    
    response = requests.get(url)
    return response.json()