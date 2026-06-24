from Building.IDocument import DocumentIdentifier
from General.ITerm import ITerm
from General.InvertedIndex import InvertedIndex
from Computing.TF import TF
from Computing.InvertedIndexCounter import InvertedIndexCounter
from Building.DocumentsHolder import DocumentsHolder

class TFdivBySum(TF):
    """
    Calculates the term frequency by dividing the term frequency in a document (f_td) by the document size |d| .
    """
    @classmethod
    def calc_tf(cls, term: ITerm, doc_id: DocumentIdentifier) -> float:
        counter: InvertedIndex = InvertedIndexCounter()  # todo, from config?
        ftd: int = counter[term][doc_id]
        d_size: int = DocumentsHolder()[doc_id].length

        return ftd/d_size


if __name__ == '__main__':
    pass
    tf = TFdivBySum()
    for k in tf:
        print(k)

    for item in tf.items():
        print(*item)



