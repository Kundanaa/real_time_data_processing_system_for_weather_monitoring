# config/settings.py
API_KEY = '3b79cba86e4f3a039776ac6df1576437'
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 60  # Time interval for API calls (in seconds)
ALERT_CHECK_INTERVAL = 5  # Check for alerts every 5 minutes
DAILY_ROLLUP_INTERVAL = 5 # Rollup every 24 hours
ALERT_THRESHOLD = {
    'temperature': 35,  # Example threshold for temperature
    'humidity': 70,     # Example threshold for humidity
    'wind_speed': 10    # Example threshold for wind speed
}