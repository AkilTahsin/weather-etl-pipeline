import requests, json, logger
from datetime import datetime
from config import WEATHER_API_KEY

def extract():
    city = "Dhaka"
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        filename = f"data/raw/weather_{city}_{datetime.now().strftime('%Y%m%d%H%M')}.json"
        with open(filename, "w") as f:
            json.dump(data, f)

        logger.info("Weather data extracted successfully")
        return filename

    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        return None
