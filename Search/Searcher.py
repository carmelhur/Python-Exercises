import logging
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)

class Searcher:
    def __init__(self, db) -> None:
        self.db = db

    def search(self, words: List[str]) -> List[Tuple[str, float]]:
        tfidf = self.db.get_tfidf()
        scores = self._calculate_scores(tfidf, words)
        top_results = self._get_top_k(scores, k=3)
        logger.info("found three highest score files")
        return top_results

    def _calculate_scores(self, tfidf: Dict[str, Dict[str, float]], words: List[str]) -> Dict[str, float]:
        all_files = sorted({f for d in tfidf.values() for f in d})
        scores: Dict[str, float] = {f: 0.0 for f in all_files}

        for word in words:
            for file, value in tfidf.get(word, {}).items():
                scores[file] += value

        logger.info("calculated combined TF-IDF scores for all files")
        return scores

    def _get_top_k(self, scores: Dict[str, float], k: int) -> List[Tuple[str, float]]:
        top_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        logger.info("sorted files by score")
        return top_results[:k]
