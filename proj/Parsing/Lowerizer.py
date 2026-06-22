from Parsing.WordBasedStringStreamTransformer import *



class Lowerizer(WordBasedStreamStringTransformer):
    @classmethod
    def _str_transform(cls, o_string: str) -> str:
        return o_string.lower()

