from numbers import Number

from InfoLogic.ICorpusInfo import ICorpusInfo
from abc import abstractmethod
from CorpusStructure.ITerm import ITerm
from CorpusStructure.IDocument import DocumentIdentifier

class Calculator(ICorpusInfo):
    @abstractmethod
    def calc(self, term: ITerm, doc_id: DocumentIdentifier) -> Number:
        raise NotImplemented("Generic Calculator doesn't have specific impolementation")

