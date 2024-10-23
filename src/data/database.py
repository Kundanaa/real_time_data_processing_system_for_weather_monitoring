# database.py
import sqlite3

# Function to establish a database connection
def db_connect():
    return sqlite3.connect('weather_data.db')

# Function to execute an INSERT query
def db_insert(conn, query, values):
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

# Function to execute a SELECT query and fetch data
def db_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Function to initialize the database tables (run once)
def initialize_database():
    conn = db_connect()
    cursor = conn.cursor()

    # Create table for raw weather data
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        temperature REAL,
        humidity REAL,
        weather TEXT,
        wind_speed REAL,
        time_of_data_update INTEGER
    )
    """)

    # Create table for daily summaries
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_summaries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        avg_temp REAL,
        max_temp REAL,
        min_temp REAL,
        dominant_condition TEXT,
        summary_date TEXT
    )
    """)

    conn.commit()
    conn.close()

