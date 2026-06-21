from abc import *
from typing import final


class ICorpusInfo(ABC):
    """
    Holds/produces info about the global corpus
    """
    '''
    @final
    #@abstractmethod
    def __init__(self):
        """
        this method is not currently abstract, but it should not be called, ever.
        """
        raise TypeError(f"trying to create instance of static class {ICorpusInfo.__name__}.")
    '''
    pass


