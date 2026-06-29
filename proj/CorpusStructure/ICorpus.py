from AppConfig import get_class_implementation
from abc import  abstractmethod
from typing import Iterator, Generic
from CorpusStructure.IDocument import IDocument, DocumentIdentifier
from CorpusStructure.ITerm import ITerm


class ICorpus(Generic[DocumentIdentifier], ):
    @classmethod
    @abstractmethod
    def get_doc_ids(cls) -> Iterator[DocumentIdentifier]:
        pass

    @classmethod
    @abstractmethod
    def get_document(cls, doc_id: DocumentIdentifier) -> IDocument:
        pass

    @classmethod
    def term_stream(cls, doc_id: DocumentIdentifier) -> Iterator[ITerm]:
        doc: IDocument = cls.get_document(doc_id)
        return doc.stream_terms()

    @classmethod
    def id_and_stream_pairs(cls) -> Iterator[tuple[DocumentIdentifier,Iterator[ITerm]]]:
        for d_id in cls.get_doc_ids():
            yield d_id, cls.term_stream(d_id)

    @classmethod
    def raw_term_stream(cls, doc_id: DocumentIdentifier):
        doc: IDocument = cls.get_document(doc_id)
        return doc.raw_term_stream()

    @classmethod
    def all_terms(cls) -> Iterator[ITerm]:
        for d_id in cls.get_doc_ids():
            for term in cls.term_stream(d_id):
                yield term

