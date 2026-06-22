from abc import *

from A_OLD.OldComputing.I_IdfCalculator import I_IdfCalculator
from Building.IDocument import DocumentIdentifier
from General.ITerm import ITerm
from A_OLD.OldComputing.ITfCalculator import ITfCalculator



class ITfIdfCalculator(ABC):
    """
    Will calculate for you the tf-idf score of a term in a document, with calc_tfidf(...) .
    Holds the "properties" tf and idf, since it seems that in all variations, the tfidf score is determined by those two.
    Since it seems to be (currently) impossible to organically have an abstract-static-property in python,
    they will be called from protected functions, _tf() and _idf(), but it's fine since they are supposed to be readonly.
    """

    @staticmethod
    @abstractmethod
    def _idf() -> I_IdfCalculator:
        pass
    @staticmethod
    @abstractmethod
    def _tf() -> ITfCalculator:
        pass

    @staticmethod
    @abstractmethod
    def calc_tfidf(term: ITerm, doc_id: DocumentIdentifier) -> float:
        pass
