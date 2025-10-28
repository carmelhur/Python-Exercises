from __future__ import annotations
from typing import Dict, List
from Indexer.Indexer import Indexer
from Processor.base_processor import BaseProcessor
import logging
logger = logging.getLogger(__name__)


class InvertedIndexer(Indexer):
    def __init__(self, base_processor: BaseProcessor) -> None:
        self.base_processor: BaseProcessor = base_processor

    def build(self, folder_path: str) -> Dict[str, Dict[str, int]]:
        processed_documents: Dict[str, List[str]] = self.base_processor.run(folder_path)
        inverted_index: Dict[str, Dict[str, int]] = {}

        for file_name, word_list in processed_documents.items():
            for word in word_list:
                if word not in inverted_index:
                    inverted_index[word] = {}
                inverted_index[word][file_name] = inverted_index[word].get(file_name, 0) + 1

        logger.info("built inverted index on files")
        return inverted_index
