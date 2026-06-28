from Building.StringTerm import StringTerm, ITerm
from Parsing.WordBasedStringStreamTransformer import WordBasedStreamStringTransformer


class Termifier(WordBasedStreamStringTransformer):
    @classmethod
    def _str_transform(cls, o_string: str) -> ITerm:
        return StringTerm(o_string)

