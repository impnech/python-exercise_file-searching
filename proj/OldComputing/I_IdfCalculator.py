from OldOrganizing.ITerm import ITerm
from OldOrganizing.IDocument import DocumentIdentifier
from abc import *


class I_IdfCalculator(ABC):

    @staticmethod
    @abstractmethod
    def idf_calc(term: ITerm, doc_id: DocumentIdentifier) -> float:
        pass

