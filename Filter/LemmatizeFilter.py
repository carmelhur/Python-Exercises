from Filter.AbstractFilter import AbstractFilter
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

class LemmatizeFilter(AbstractFilter):
    KEEP = {"is", "am", "are"}

    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def get_wordnet_pos(self, tag):
        if tag.startswith('J'): return wordnet.ADJ
        if tag.startswith('V'): return wordnet.VERB
        if tag.startswith('N'): return wordnet.NOUN
        if tag.startswith('R'): return wordnet.ADV
        return wordnet.NOUN

    def filtering(self, tokens):
        results = []
        for w in tokens:
            if w in self.KEEP:
                results.append(w)
                continue
            for word_text, tag in pos_tag([w]):
                wn_pos = self.get_wordnet_pos(tag)
                lemma = self.lemmatizer.lemmatize(word_text, wn_pos)
                results.append(lemma)
        return results
