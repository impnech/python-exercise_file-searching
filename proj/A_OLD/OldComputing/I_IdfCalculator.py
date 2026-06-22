from General.ITerm import ITerm
from Building.IDocument import DocumentIdentifier
from abc import *


class I_IdfCalculator(ABC):

    @staticmethod
    @abstractmethod
    def idf_calc(term: ITerm, doc_id: DocumentIdentifier) -> float:
        pass

