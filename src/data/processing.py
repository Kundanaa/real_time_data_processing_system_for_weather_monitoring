from collections import Counter
from datetime import datetime
#from data.storage import store_daily_summary

def most_common(data):
    if data:
        return Counter(data).most_common(1)[0][0]  # Returns the most common element
    return None  # If the list is empty, return None

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(data):
    # Debugging: Print the full response for analysis
    #print("Full API Response:", data)

    if "name" in data and "main" in data and "weather" in data:
        processed_data = {
            "city": data["name"],
            "temperature": round(kelvin_to_celsius(data["main"]["temp"]),2),
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "wind_speed":data["wind"]["speed"],
            "time_of_data_update": data["dt"]
        }
        return processed_data
    else:
        print("Error: Missing key data in the API response.")
        print("Full Response:", data)  # Log the full response for debugging
        return None

def calculate_daily_summary(daily_data):
    if not daily_data:
        return None
    temps = [entry[1] for entry in daily_data]
    summary= {
        "avg_temp": sum(temps) / len(temps),
        "max_temp": max(temps),
        "min_temp": min(temps),
        "dominant_condition": most_common([entry[3] for entry in daily_data]),
        "summary_date": datetime.now().strftime('%Y-%m-%d')
    }
    #store_daily_summary(summary)
    return summary


