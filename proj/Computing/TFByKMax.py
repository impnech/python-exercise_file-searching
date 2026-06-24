from Computing.InvertedIndexCounter import InvertedIndexCounter
from Building.DocumentsHolder import DocumentsHolder, DocumentIdentifier, IDocument
from TF import *
from Computing.MaxFtd import MaxFtd, InfoPerDocument


class TFByKMax(TF):
    def __init__(self, K: float = 0.5):
        super().__init__()
        if K < 0 or K > 1:
            raise ValueError(f"K must be in [0,1], but got {K}")
        self._K: float = K
    @classmethod
    def calc_tf(cls, term: ITerm, doc_id: DocumentIdentifier) -> float:
        counter: InvertedIndex[Mapping[DocumentIdentifier,int]] = InvertedIndexCounter()
        maxer: InfoPerDocument[DocumentIdentifier, int] = MaxFtd()
        weight = counter[term][doc_id] / maxer[doc_id]
        return cls._K + (1 - cls._K) * weight


if __name__ == "__main__":
    pass
    tf = TFByKMax(0.3)
    for k in TFByKMax().items():
        print(k)
