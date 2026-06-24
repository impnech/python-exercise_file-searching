from General.InvertedIndex import InvertedIndex , ITerm, DH
from abc import abstractmethod
from Building.DocumentsHolder import DocumentsHolder, DocumentIdentifier

class IDF(InvertedIndex[float]):
    """
    for most of variation i saw, idf is not dependent on a specific document.
    for the possible exception, it's acceptable to handle seperatly
    """
    @abstractmethod
    def calc_idf(self, term: ITerm) -> float:
        raise NotImplementedError(f"Generic IDF doesn't have calculation implementation")

    def reset(self):
        for term in DocumentsHolder().get_all_terms_with_duplicates():
            if term in self._dict_handler:
                continue
            self._dict_handler[term] = self.calc_idf(term)


if __name__ == '__main__':
    pass 
