import requests
from api.config.settings import API_KEY

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        
        # Ensure the response contains necessary fields
        if "main" in data and "weather" in data:
            return data
        else:
            print(f"Error: Missing weather information in the response for {city}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data for {city}: {e}")
        return None
    #response = requests.get(url)
    #return response.json()
