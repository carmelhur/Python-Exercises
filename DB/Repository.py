class Repository:
    def __init__(self):
        self._index= {}
        self._tfidf= {}

    def store_index(self, index):
        self._index = index

    def store_tfidf(self, tfidf):
        self._tfidf = tfidf


    def get_tfidf(self) :
        return self._tfidf

