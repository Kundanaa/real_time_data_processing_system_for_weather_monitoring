# Real_time_data_processing_system_for_weather_monitoring
real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system will utilize data from the OpenWeatherMap API ( https://openweathermap.org/ ).

## Data Source:
The system will continuously retrieve weather data from the OpenWeatherMap API. You will
need to sign up for a free API key to access the data. The API provides various weather
parameters, and for this assignment, we will focus on:

1. main: Main weather condition (e.g., Rain, Snow, Clear)
2. temp: Current temperature in Centigrade
3. feels_like: Perceived temperature in Centigrade
4. dt: Time of the data update (Unix timestamp)

## Processing and Analysis:

1. The system should continuously call the OpenWeatherMap API at a configurable interval
(e.g., every 5 minutes) to retrieve real-time weather data for the metros in India. (Delhi,
Mumbai, Chennai, Bangalore, Kolkata, Hyderabad)
2. For each received weather update:
     1. Convert temperature values from Kelvin to Celsius (tip: you can also use user preference).

## Rollups and Aggregates:

1. Daily Weather Summary:
   1. Roll up the weather data for each day.
   2. Calculate daily aggregates for:
        1. Average temperature
        2. Maximum temperature
        3. Minimum temperature
        4. Dominant weather condition 
   3. Store the daily summaries in a database or persistent storage for further analysis.
      
2. Alerting Thresholds:
    1. Define user-configurable thresholds for temperature or specific weather
       conditions (e.g., alert if temperature exceeds 35 degrees Celsius for two
       consecutive updates).
    2. Continuously track the latest weather data and compare it with the thresholds.
    3. If a threshold is breached, trigger an alert for the current weather conditions.
Alerts could be displayed on the console or sent through an email notification
system (implementation details left open-ended).

3. Implement visualizations:
     1.  To display daily weather summaries, historical trends, and triggered alerts.

## Test Cases:

1. System Setup:
     1. Verify system starts successfully and connects to the OpenWeatherMap API
         using a valid API key.

2. Data Retrieval:
     1. Simulate API calls at configurable intervals.
     2. Ensure the system retrieves weather data for the specified location and parses
         the response correctly.

3. Temperature Conversion:
      1. Test conversion of temperature values from Kelvin to Celsius (or Fahrenheit)
        based on user preference.

4. Daily Weather Summary:
      1. Simulate a sequence of weather updates for several days.
      2. Verify that daily summaries are calculated correctly, including average, maximum,
          minimum temperatures, and dominant weather condition.

5. Alerting Thresholds:
      1. Define and configure user thresholds for temperature or weather conditions.
      2. Simulate weather data exceeding or breaching the thresholds.
      3. Verify that alerts are triggered only when a threshold is violated.
