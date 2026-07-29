# Weather Logger

A Python script that automatically collects current weather data for 10 U.S. cities every hour using the OpenWeatherMap API, and logs it to a CSV file for historical tracking and analysis.

## What it does

- Fetches live weather data (temperature, humidity, wind speed, conditions) for a configurable list of cities
- Appends each reading to `data/weather_log.csv` with a timestamp
- Handles API/network failures gracefully without crashing the whole run
- Logs all activity (successes and failures) to `weather_log.log`
- Runs automatically every hour via cron — no manual intervention needed
- Includes a separate analysis script (`analyze.py`) using pandas to summarize trends across cities

## Setup

1. Clone the repo:
```bash
   git clone https://github.com/drewtwosunny/weather-logger.git
   cd weather-logger
```

2. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)

5. Create a `.env` file in the project root (see `.env.example`):
```
   OPENWEATHER_API_KEY=your_actual_key_here
```

## Running it manually

```bash
python3 main.py
```

## Running the analysis

```bash
python3 analyze.py
```

## Automating with cron

To run automatically every hour, add this to your crontab (`crontab -e`), replacing the paths with your own absolute paths:

```
0 * * * * cd "/path/to/weather-logger" && "/path/to/weather-logger/venv/bin/python3" main.py >> cron.log 2>&1
```

## Project structure

```
weather-logger/
├── main.py              # fetches and logs weather data
├── analyze.py             # pandas analysis of collected data
├── requirements.txt      # dependencies
├── .env.example           # template for required environment variables
├── .gitignore
└── data/
    └── weather_log.csv   # generated data (not committed)
```