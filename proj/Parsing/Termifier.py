from CorpusStructure.StringTerm import StringTerm, ITerm
from Parsing.WordBasedStringStreamTransformer import WordBasedStreamStringTransformer


class Termifier(WordBasedStreamStringTransformer):
    @classmethod
    def _str_transform(cls, o_value) -> ITerm:
        raise NotImplementedError("Termifier is generic")

