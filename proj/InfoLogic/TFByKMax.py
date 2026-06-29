from typing import Mapping

from InfoLogic.InvertedIndexCounter import InvertedIndexCounter
from CorpusStructure.DocumentsHolder import DocumentsHolder, DocumentIdentifier, IDocument
from InfoLogic.TF import *
from InfoLogic.MaxFtd import MaxFtd, InfoPerDocument


class TFByKMax(TF):
    """
    (1-k)*n_t/max_{t' in d}(n_t') + k 
    (0<k<1)
    by default k is 0.5, and it shouldn't be changed mid-run.
    """

    # for now K can be only 0.5, todo better (not urgent)
    @property
    def K(self):
        return 0.5

    def calc_for_new(self, term: ITerm, doc_id: DocumentIdentifier) -> float:
        counter: InvertedIndex[Mapping[DocumentIdentifier,int]] = InvertedIndexCounter()
        maxer: InfoPerDocument[DocumentIdentifier, int] = MaxFtd()
        weight = counter[term][doc_id] / maxer[doc_id]
        k = self.K
        return k + (1 - k) * weight


if __name__ == "__main__":
    pass
    tf = TFByKMax()
    for k in TFByKMax().items():
        print(k)
