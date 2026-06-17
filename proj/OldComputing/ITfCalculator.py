from abc import *
from OldOrganizing.ITerm import ITerm
from OldOrganizing.IDocument import *


class ITfCalculator(ABC):
    @staticmethod
    @abstractmethod
    def calc_tf(term: ITerm, doc_id: DocumentIdentifier):
        pass

