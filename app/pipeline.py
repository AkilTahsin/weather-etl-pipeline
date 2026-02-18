from extract import extract
from transform import transform
from load import load
import logger

def run_pipeline():
    logger.init()
    logger.info("Weather ETL pipeline started")

    raw_file = extract()
    if raw_file:
        processed_file = transform(raw_file)
        if processed_file:
            load(processed_file)

    logger.info("Weather ETL pipeline finished")

if __name__ == "__main__":
    run_pipeline()
