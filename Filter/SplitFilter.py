from Filter.AbstractFilter import AbstractFilter
class SplitFilter(AbstractFilter):
    def filtering(self, text):
        return [word.strip() for word in text.split() if word.strip()]