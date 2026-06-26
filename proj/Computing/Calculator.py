from numbers import Number

from General.ICorpusInfo import ICorpusInfo
from abc import abstractmethod
from General.ITerm import ITerm
from Building.IDocument import DocumentIdentifier

class Calculator(ICorpusInfo):
    @abstractmethod
    def calc(term: ITerm, doc_id: DocumentIdentifier) -> Number:
        raise NotImplemented("Generic Calculator doesn't have specific impolementation")

