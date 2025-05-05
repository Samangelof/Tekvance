import logging
import os
from logging.handlers import RotatingFileHandler


LOG_PATH = "logs"
os.makedirs(LOG_PATH, exist_ok=True)

LOG_LEVEL = logging.DEBUG

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"

def setup_logging():
    rotating_handler = RotatingFileHandler(
        os.path.join(LOG_PATH, 'app.log'),
        maxBytes=10*1024*1024,
        backupCount=5,
        encoding='utf-8'
    )
    rotating_handler.setLevel(LOG_LEVEL)
    rotating_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=LOG_DATEFMT))

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=LOG_DATEFMT))

    logger = logging.getLogger('TekvanceApp')
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(rotating_handler)
    logger.addHandler(console_handler)

    return logger


#? Example
# logger = setup_logging()
# logger.info("Приложение запущено.")
# logger.warning("Это предупреждение.")
# logger.error("Ошибка!")