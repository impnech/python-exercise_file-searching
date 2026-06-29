from CorpusStructure.ITerm import *
from Computing.DictUsingInfo import *
from typing import *

TermInfo = TypeVar('TermInfo')
class InvertedIndex(DictUsingInfo[ITerm, TermInfo], Generic[TermInfo]):
    pass


if __name__ == '__main__':
    pass

