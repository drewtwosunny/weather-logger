import os
import csv
import logging
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

logging.basicConfig(
    filename="weather_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def save_to_csv(city, temperature, humidity, description, wind_speed, filename="data/weather_log.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "city", "temperature", "humidity", "description", "wind_speed"])

        writer.writerow([datetime.now(), city, temperature, humidity, description, wind_speed])


url = "https://api.openweathermap.org/data/2.5/weather"

cities = [
    "Chicago", "New York", "Los Angeles", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "Tulsa", "Dallas", "Miami"
]

for city in cities:
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error fetching {city}: {e}")
        continue

    if response.status_code == 200:
        data = response.json()

        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        logging.info(f"{city_name}: {temperature}°F, {description}, humidity {humidity}%, wind {wind_speed} mph")

        save_to_csv(city_name, temperature, humidity, description, wind_speed)
    else:
        logging.warning(f"Failed to get data for {city}: status code {response.status_code}")
