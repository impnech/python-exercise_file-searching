from Computing.InvertedIndexCounter import InvertedIndexCounter
from Building.DocumentsHolder import DocumentsHolder, DocumentIdentifier
from TF import *


class TFByKMax(TF):
    @classmethod
    def calc_tf(cls, term: ITerm, doc_id: DocumentIdentifier) -> float:
        counter: InvertedIndex[Mapping[DocumentIdentifier,int]] = InvertedIndexCounter()
        doc: IDocument = DocumentsHolder()[doc_id]
        doc.stream_terms()


