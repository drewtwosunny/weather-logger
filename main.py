import os
import csv
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

# Retrieve the API key we just loaded
api_key = os.getenv("OPENWEATHER_API_KEY")

def save_to_csv(city, temperature, humidity, description, wind_speed, filename="data/weather_log.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "city", "temperature", "humidity", "description", "wind_speed"])

        writer.writerow([datetime.now(), city, temperature, humidity, description, wind_speed])


# The endpoint we're calling
url = "https://api.openweathermap.org/data/2.5/weather"

# Query parameters — requests will build the full URL from this dict
params = {
    "q": "Chicago",
    "appid": api_key,
    "units": "imperial"
}

response = requests.get(url, params=params)

# Convert the JSON response body into a Python dict
data = response.json()

print(data)

city = data['name']
temperature = data['main']['temp']
humidity = data['main']['humidity']
description = data['weather'][0]['description']
wind_speed = data['wind']['speed']

print(f"{city}: {temperature}°F, {description}, humidity {humidity}%, wind {wind_speed} mph")
save_to_csv(city, temperature, humidity, description, wind_speed)