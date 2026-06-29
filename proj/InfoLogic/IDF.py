from InfoLogic.InvertedIndex import InvertedIndex , ITerm
from abc import abstractmethod
from numbers import Number
from CorpusStructure.DocumentsHolder import DocumentsHolder
from DesignPatterns.DefaultHolder import DefaultHolder

class IDF(InvertedIndex[Number],DefaultHolder):
    """
    for most of variation i saw, idf is not dependent on a specific document.
    for the possible exception, it's acceptable to handle seperatly
    """

    def __init__(self, default_value = 0):
        super().__init__(default_value)

    @abstractmethod
    def calc_idf(self, term: ITerm) -> Number:
        raise NotImplementedError(f"Generic IDF doesn't have calculation implementation")


    def safe_calc_idf(self,term: ITerm) -> Number:
        try:
            return self.calc_idf(term)
        except KeyError:
            return self.default_value

    def reset(self):
        
        for term in DocumentsHolder().get_all_terms_with_duplicates():
            if term in self._dict_handler:
                continue
            self._dict_handler[term] = self.calc_idf(term)


if __name__ == '__main__':
    pass 

