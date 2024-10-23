import schedule
import time
from visualizations.visualize import generate_daily_visualization
from alerts.altering import check_thresholds
from api.openweather import get_weather_data
from data.processing import process_weather_data, calculate_daily_summary
from api.config.settings import CITIES, INTERVAL, ALERT_THRESHOLD
from data.storage import store_weather_data, store_daily_summary, fetch_past_summaries,fetch_daily_weather_data

def job():
    print("Fetching weather data...")
    for city in CITIES:
        data = get_weather_data(city)
        processed_data = process_weather_data(data)
        if processed_data:
            # Updated the key to match the dictionary returned by process_weather_data
            print(f"Weather in {city}: Temperature {processed_data['temperature']}°C, "
                f"Feels like {processed_data['weather']}, "
                f"Humidity: {processed_data['humidity']}, "
                f"Wind Speed: {processed_data['wind_speed']}, "
                f"Time of data update: {processed_data['time_of_data_update']}")
            check_thresholds(processed_data, ALERT_THRESHOLD)
            store_weather_data(processed_data)
        else:
            print(f"Failed to process weather data for {city}.")

schedule.every(INTERVAL).seconds.do(job)

def rollup_daily_summary():
    try:
        daily_data = fetch_daily_weather_data()  # Fetch data from storage
        if daily_data:
            summary = calculate_daily_summary(daily_data)
            print(f"Daily Summary: {summary}")
            store_daily_summary(summary)  # Store the summary
        else:
            print("No data available for the day.")
    except Exception as e:
        print(f"Error in rollup_daily_summary: {e}")

#schedule.every().day.at("23:59").do(rollup_daily_summary)
schedule.every(INTERVAL).seconds.do(rollup_daily_summary)

def visualize_summaries():
    try:
        summaries = fetch_past_summaries()  # Fetch past data
        if summaries:
            generate_daily_visualization(summaries)  # Generate visualization
        else:
            print("No data available for visualization.")
    except Exception as e:
        print(f"Error in visualize_summaries: {e}")

# Schedule the visualization for the end of the week, or anytime you want
#schedule.every().monday.at("10:00").do(visualize_summaries)  # Weekly visualization
schedule.every(INTERVAL).seconds.do(visualize_summaries)

while True:
    schedule.run_pending()
    time.sleep(1)
