import string
from Filter.AbstractFilter import AbstractFilter

class PunctuationFilter(AbstractFilter):
    def filtering(self, text: str):
        return text.translate(str.maketrans('', '', string.punctuation))
