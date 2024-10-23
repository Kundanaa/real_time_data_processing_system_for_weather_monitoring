# storage.py
from data.database import db_connect, db_insert, db_query
#from data.processing import process_weather_data
# Function to store raw weather data fetched from the API
def store_weather_data(processed_data):
    conn = db_connect()
    query = """
    INSERT INTO weather_data (city, temperature, humidity, weather, wind_speed, time_of_data_update)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    values = (processed_data["city"], processed_data["temperature"],processed_data["humidity"], processed_data["weather"], processed_data["wind_speed"], processed_data["time_of_data_update"])
    print(f"Inserting data into DB: {values}")  # Add this line to check values
    db_insert(conn, query, values)
    conn.close()

# Function to fetch weather data for the day (used for daily summary rollup)
def fetch_daily_weather_data():
    conn = db_connect()
    query = """
    SELECT city, temperature, humidity, weather, wind_speed FROM weather_data
    WHERE date(datetime(time_of_data_update, 'unixepoch', 'localtime')) = date('now', 'localtime')
    """
    daily_data = db_query(conn, query)
    conn.close()
    return daily_data

# Function to store the daily summary
def store_daily_summary(summary):
    conn = db_connect()
    query = """
    INSERT INTO daily_summaries (avg_temp, max_temp, min_temp, dominant_condition, summary_date)
    VALUES (?, ?, ?, ?, ?)
    """
    values = (summary["avg_temp"], summary["max_temp"], summary["min_temp"], summary["dominant_condition"], summary["summary_date"])
    db_insert(conn, query, values)
    conn.close()

# Function to fetch past daily summaries for visualization
def fetch_past_summaries():
    conn = db_connect()  # Establish connection
    query = """
    SELECT avg_temp, max_temp, min_temp, dominant_condition, summary_date 
    FROM daily_summaries
    ORDER BY summary_date DESC 
    LIMIT 30  
    """
    past_summaries = db_query(conn, query)  # Fetch data
    conn.close()  # Close connection
    return past_summaries

