from Building.IDocument import *
from typing import Iterable
from General.DIDAndStreamsGenerator import DIDAndStreamsGenerator
from General.DocumentManager import *
from pathlib import Path

class DocumentByPath(IDocument[Path]):
    """
    """

    __length: int

    @property
    def length(self) -> int:
        try:
            return self.__length
        except AttributeError:
            self.__length = sum(1 for _ in self.stream_terms())
            return self.__length

    def __init__(self, doc_id: Path) -> None:
        IDocument.__init__(self, doc_id)

    def stream_terms(self) -> Iterator[ITerm]:
        return DIDAndStreamsGenerator.stream_overall_transformation(get_word_stream(self.doc_id))
