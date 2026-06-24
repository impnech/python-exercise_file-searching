from General.DictHandler import DictHandler

from General.ITerm import *
from General.DictUsingInfo import *
from typing import *

TermInfo = TypeVar('TermInfo')
class InvertedIndex(DictUsingInfo[ITerm, TermInfo], Generic[TermInfo]):
    pass
if __name__ == '__main__':


    pass