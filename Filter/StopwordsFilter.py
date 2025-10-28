from Filter.AbstractFilter import AbstractFilter

class StopwordsFilter(AbstractFilter):
    def __init__(self, filepath):
        with open(filepath, "r", ) as f:
            self.stopwords = set(line.strip().lower() for line in f if line.strip())

    def filtering(self, text):
        words = text.split()
        filtered = [w for w in words if w.lower() not in self.stopwords]
        return " ".join(filtered)
