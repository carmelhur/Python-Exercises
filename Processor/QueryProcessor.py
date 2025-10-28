import logging
from typing import List
from Processor.base_processor import BaseProcessor
from Processor.Processor_function import apply_filters

logger = logging.getLogger(__name__)

class QueryProcessor(BaseProcessor):
    def __init__(self, stopwords_path: str) -> None:
        super().__init__()
        self.stopwords_path: str = stopwords_path

    def run(self, text: str) -> List[str]:
        logger.info("Processing user query")
        tokens: List[str] = apply_filters(text, self.stopwords_path)
        logger.info("Query tokens after filtering")
        return tokens
