import pandas as pd
import json, logger

def transform(raw_file):
    try:
        with open(raw_file) as f:
            data = json.load(f)

        record = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "timestamp": pd.Timestamp.now()
        }

        df = pd.DataFrame([record])

        processed_file = raw_file.replace("raw", "processed").replace(".json", ".csv")
        df.to_csv(processed_file, index=False)

        logger.info("Weather data transformed successfully")
        return processed_file

    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        return None
