def check_thresholds(processed_data, thresholds):
    temp_threshold = thresholds.get('temperature')
    humidity_threshold = thresholds.get('humidity')
    wind_speed_threshold = thresholds.get('wind_speed')

    # Check temperature threshold
    if temp_threshold and processed_data['temperature'] > temp_threshold:
        print(f"Alert: Temperature in {processed_data['city']} is above {temp_threshold}°C!")

    # Check humidity threshold
    if humidity_threshold and processed_data.get('humidity') > humidity_threshold:
        print(f"Alert: Humidity in {processed_data['city']} is above {humidity_threshold}%!")

    # Check wind speed threshold
    if wind_speed_threshold and processed_data.get('wind_speed') > wind_speed_threshold:
        print(f"Alert: Wind speed in {processed_data['city']} is above {wind_speed_threshold} m/s!")
