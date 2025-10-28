import math
from collections import defaultdict
from typing import Dict
from Score.Score import Score


class TFIDFScore(Score):
    def calculate(self, index: Dict[str, Dict[str, int]]) -> Dict[str, Dict[str, float]]:
        lenfiles = self._calc_tf(index)
        total_docs = len({f for files in index.values() for f in files})
        final_scores: Dict[str, Dict[str, float]] = {}

        for word, files_by_word in index.items():
            idf = self._calc_idf(total_docs, len(files_by_word))
            scores = self._calc_tfidf(files_by_word, lenfiles, idf)
            final_scores[word] = scores

        return final_scores

    def _calc_tf(self, index: Dict[str, Dict[str, int]]) -> Dict[str, int]:
        lenfiles: Dict[str, int] = defaultdict(int)
        for files_by_word in index.values():
            for file_name, count in files_by_word.items():
                lenfiles[file_name] += count
        return lenfiles

    def _calc_idf(self, total_docs: int, doc_freq: int) -> float:
        return math.log10(total_docs / doc_freq)

    def _calc_tfidf(self, files_by_word: Dict[str, int], lenfiles: Dict[str, int], idf: float) -> Dict[str, float]:
        scores: Dict[str, float] = {}
        for file_name, count in files_by_word.items():
            tf = count / lenfiles[file_name]
            scores[file_name] = tf * idf
        return scores
