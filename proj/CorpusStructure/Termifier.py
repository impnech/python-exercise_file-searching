from CorpusStructure.ITerm import ITerm
from CorpusStructure.StreamTermifier import StreamTermifier

class Termifier(StreamTermifier):

    @classmethod
    def transform(cls, original: Iterator | Iterable) -> Iterator[ITerm]:
        return (cls._str_transform(x) for x in original)
    @classmethod
    def _str_transform(cls, o_value) -> ITerm:
        raise NotImplementedError("Termifier is generic")

