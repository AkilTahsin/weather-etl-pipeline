import pandas as pd
import logger
from sqlalchemy import create_engine
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

def load(processed_file):
    try:
        df = pd.read_csv(processed_file)

        engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

        df.to_sql("weather_data", engine, if_exists="append", index=False)

        logger.info("Weather data loaded into PostgreSQL")

    except Exception as e:
        logger.error(f"Loading failed: {e}")
