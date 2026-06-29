from typing import Iterator, Iterable

from AppConfig import get_class_implementations_list
from CorpusStructure.StringTerm import StringTerm
from CorpusStructure.Termifier import Termifier, ITerm
from EnvManager import force_get_env
from Parsing.StringStreamTransformer import StringStreamTransformer


class TermifierToStringTerm(Termifier):

    transformers_list: list[StringStreamTransformer] = get_class_implementations_list(StringStreamTransformer.__name__)
    @classmethod
    def _transform(cls, iterator: Iterator[str] | Iterable[str]):
        res = iterator
        for transformer in cls.transformers_list:
            res = transformer.transform(res)
        return res
    @classmethod
    def termify_by_one(cls, o_value) -> ITerm:
        return StringTerm(o_value)

