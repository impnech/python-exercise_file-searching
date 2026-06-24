from abc import *
from typing import final

from General.Singleton import Singleton


class ICorpusInfo(Singleton):
    """
    Holds/produces info about the global corpus
    """

    @abstractmethod
    def reset(self):   
        """
        We do want to hold information about the corpus, but we have to be prepared to a possible change in the corpus, thus we need to be able to reset the information we hold about it.
        if for some subclass, it's not relevant, then it should implement this method as a nop (pass)
        """
        raise NotImplementedError(f"Generic ICorpusInfo doesn't have reset implementation")

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


