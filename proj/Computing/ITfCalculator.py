from abc import *
from Organizing.ITerm import ITerm
from Organizing.IDocument import *


class ITfCalculator(ABC):
    @staticmethod
    @abstractmethod
    def calc_tf(term: ITerm, doc_id: DocumentIdentifier):
        pass

