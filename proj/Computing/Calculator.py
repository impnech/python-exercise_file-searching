from numbers import Number

from General.ICorpusInfo import ICorpusInfo
from abc import abstractmethod
from Building.ITerm import ITerm
from Building.IDocument import DocumentIdentifier

class Calculator(ICorpusInfo):
    @abstractmethod
    def calc(self, term: ITerm, doc_id: DocumentIdentifier) -> Number:
        raise NotImplemented("Generic Calculator doesn't have specific impolementation")

