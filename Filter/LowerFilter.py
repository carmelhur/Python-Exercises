from Filter.AbstractFilter import AbstractFilter


class LowerFilter(AbstractFilter):
    def filtering(self, text):
        return text.lower()
