# ==========================================
# Weather Information Retrieval Using API
# ==========================================

# Import required modules
import requests
import json

# Weather API URL
url = "https://wttr.in/Dhaka?format=j1"

try:
    # Send GET request to the API
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:

        # Convert response to JSON
        weather_data = response.json()

        # Extract required information
        city = "Dhaka"
        temperature = weather_data["current_condition"][0]["temp_C"]
        weather_desc = weather_data["current_condition"][0]["weatherDesc"][0]["value"]
        humidity = weather_data["current_condition"][0]["humidity"]
        wind_speed = weather_data["current_condition"][0]["windspeedKmph"]

        # Display weather information
        print("=" * 40)
        print("        Weather Information")
        print("=" * 40)
        print(f"City Name          : {city}")
        print(f"Temperature        : {temperature}°C")
        print(f"Weather Condition  : {weather_desc}")
        print(f"Humidity           : {humidity}%")
        print(f"Wind Speed         : {wind_speed} km/h")
        print("=" * 40)

    else:
        print("Error: Unable to retrieve weather data.")

except requests.exceptions.RequestException as e:
    print("Request Failed!")
    print("Error:", e)
