from CorpusStructure.IDocument import *
from typing import Iterable
from FileUsers.IDsAndStreamsGenerator import IDsAndStreamsGenerator
from FileUsers.FileManager import get_word_stream
from pathlib import Path

class DocumentByStream(IDocument[Path]):
    """
    doesn't hold the terms in memory
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
        return IDsAndStreamsGenerator.stream_overall_transformation(get_word_stream(self.doc_id))


if __name__ == '__main__':
    doc = DocumentByStream(Path(__file__).parent.parent/Path(r'files/sample_texts/file1.txt'))
    g=doc.stream_terms()
    x =next(g)
    print(x)

