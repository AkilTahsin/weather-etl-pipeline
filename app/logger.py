import logging, datetime

def init():
    logging.basicConfig(
        filename="logs/pipeline.log",
        level=logging.INFO,
        format="%(message)s"
    )
    logging.basicConfig(
        filename="logs/pipeline.log",
        level=logging.ERROR,
        format="%(message)s"
    )

def info(message):
    logging.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | INFO  | {message}")

def error(message):
    logging.error(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | ERROR | {message}")
