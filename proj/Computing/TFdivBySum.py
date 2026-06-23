from Building.IDocument import DocumentIdentifier
from General.ITerm import ITerm
from General.InvertedIndex import InvertedIndex
from TF import TF
from Computing.InvertedIndexCounter import InvertedIndexCounter
from Building.DocumentsHolder import DocumentsHolder

class TFdivBySum(TF):
    @classmethod
    def calc_tf(cls, term: ITerm, doc_id: DocumentIdentifier) -> float:
        counter: InvertedIndex = InvertedIndexCounter()  # todo, from config?
        ftd: int = counter[term][doc_id]
        d_size: int = DocumentsHolder()[doc_id].length

        return ftd/d_size


if __name__ == '__main__':
    pass
    tf_calc = TFdivBySum()



