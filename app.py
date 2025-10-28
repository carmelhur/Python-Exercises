from Logs.LoggerConfig import LoggerConfig
LoggerConfig.setup()
from Processor.base_processor import BaseProcessor
from Processor.QueryProcessor import QueryProcessor
from Indexer.Indexer import Indexer
from Indexer.inverted_indexr import InvertedIndexer
from DB.Repository import Repository
from Score.TFIDFScore import TFIDFScore
from Search.Searcher import Searcher
import logging

logger = logging.getLogger(__name__)


class App:
    def __init__(self, folder_path, stopwords_path, processor: BaseProcessor):
        self.folder_path = folder_path
        self.stopwords_path = stopwords_path
        self.processor = processor
        self.indexer: Indexer = InvertedIndexer(self.processor)

    def run(self):
        try:
            db = Repository()
            logger.info("Built repository")

            index = self.indexer.build(self.folder_path)
            db.store_index(index)
            logger.info("Stored inverted index")

            tfidf_scores = TFIDFScore().calculate(index)  # <- use the new class
            db.store_tfidf(tfidf_scores)
            logger.info("Stored TF-IDF")

            qp = QueryProcessor(self.stopwords_path)
            searcher = Searcher(db)

            q = input("Enter query : ").strip()
            if not q:
                logger.info("Empty query")
                return

            logger.info("Got query from user")
            words = qp.run(q)
            logger.info("query has been filterd")

            results = list(searcher.search(words))
            if not results:
                logger.info("No results")
            else:
                for f, w in results:
                    print(f"{f}: {w:.5f}")
                print()
                logger.info("result has been printed")

        except FileNotFoundError as e:
            logger.error(f"File not found: {e}")
            print("file or directory path is not found")
