import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class LoggerConfig:
    LOG_FILE = Path("Logs/logs.log")

    @staticmethod
    def setup():
        LoggerConfig.LOG_FILE.parent.mkdir(exist_ok=True)

        handler_file = RotatingFileHandler(
            LoggerConfig.LOG_FILE, maxBytes=1_000_000, backupCount=3, encoding="utf-8"
        )

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            handlers=[handler_file],
        )

        logging.getLogger(__name__).info("Logging started")
