import matplotlib.pyplot as plt
from data.storage import fetch_past_summaries

def generate_daily_visualization(summaries):
    # Fetch the daily summary from the database
    daily_data = fetch_past_summaries()

    # Example: Visualize temperature trends for the day
    temps = [entry[0] for entry in daily_data]
    dates = [entry[4] for entry in daily_data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, temps, marker='o', label='Average Temperature')
    plt.title('Daily Temperature Trends')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.savefig('daily_weather_summary.png')
    plt.show()

