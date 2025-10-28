from Logs.LoggerConfig import LoggerConfig

LoggerConfig.setup()
from Processor.FileProcessor import FileProcessor
from dotenv import load_dotenv
import os
import logging
from app import App

logger = logging.getLogger(__name__)


def main():
    load_dotenv()
    sample_path = os.getenv("SAMPLE_TEXT_PATH")
    stopwords_path = os.getenv("STOPWORDS_PATH")
    processor = FileProcessor(stopwords_path)
    app = App(sample_path, stopwords_path, processor)
    app.run()


if __name__ == "__main__":
    main()
