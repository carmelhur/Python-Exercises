from __future__ import annotations
import os
import logging
from typing import Dict, List
from Processor.base_processor import BaseProcessor
from Processor.Processor_function import apply_filters
from Processor.ProcessChecking import ProcessChecking

logger = logging.getLogger(__name__)

class FileProcessor(BaseProcessor):
    def __init__(self, stopwords_path: str) -> None:
        super().__init__()
        self.stopwords_path: str = stopwords_path
        self.checker = ProcessChecking()

    def run(self, dir_path: str) -> Dict[str, List[str]]:
        result: Dict[str, List[str]] = {}

        if not self.checker.validate_directory(dir_path):
            return result

        for name in os.listdir(dir_path):
            fp = os.path.join(dir_path, name)
            try:
                logger.info("Started filtering file: %s", name)
                with open(fp, "r", encoding="utf-8") as f:
                    content = f.read()
                tokens = apply_filters(content, self.stopwords_path)
                result[name] = tokens
                logger.info("Finished filtering file: %s", name)
            except Exception:
                logger.exception("Error while processing file: %s", name)

        logger.info("Applied filters on all files in directory: %s", dir_path)
        return result
