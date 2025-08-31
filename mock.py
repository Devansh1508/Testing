import requests

def get_weather(city):
    response = requests.get(f"http://api.weatherapi.com/v1/{city}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("could not fetch weather data")