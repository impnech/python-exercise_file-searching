from abc import abstractmethod, ABC

from General.ITerm import ITerm
from General.InvertedIndex import InvertedIndex


class TF(InvertedIndex):

    @classmethod
    @abstractmethod
    def calc_tf(cls, term: ITerm) -> float:
        pass
    #todo soon add dict association




if __name__ == '__main__':
    pass

