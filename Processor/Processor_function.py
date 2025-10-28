from typing import List
from Processor.pipeline import Pipeline
from Filter.PunctuationFilter import PunctuationFilter
from Filter.LowerFilter import LowerFilter
from Filter.StopwordsFilter import StopwordsFilter
from Filter.SplitFilter import SplitFilter
from Filter.LemmatizeFilter import LemmatizeFilter


def build_pipeline(stopwords_path: str) -> Pipeline:
    return (
        Pipeline()
        .add_filter(PunctuationFilter())
        .add_filter(LowerFilter())
        .add_filter(StopwordsFilter(stopwords_path))
        .add_filter(SplitFilter())
        .add_filter(LemmatizeFilter())
    )


def apply_filters(text: str, stopwords_path: str) -> List[str]:
    pipeline = build_pipeline(stopwords_path)
    tokens: List[str] = pipeline.process(text)
    return tokens
