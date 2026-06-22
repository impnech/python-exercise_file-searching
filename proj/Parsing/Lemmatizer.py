from Parsing.WordBasedStringStreamTransformer import *
import nltk
import spacy


class Lemmatizer(WordBasedStreamStringTransformer):
    @classmethod
    def _str_transform(cls, o_string: str) -> str:
        raise NotImplemented("Lemmatizer")