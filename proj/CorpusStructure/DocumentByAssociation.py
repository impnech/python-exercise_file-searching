from typing import Any, Iterator

from CorpusStructure.IDocument import IDocument, ITerm , DocumentIdentifier
from pathlib import Path

from FileUsers.FileManager import get_word_stream
from FileUsers.IDsAndStreamsGenerator import IDsAndStreamsGenerator
from Loggers.g_logging import g_logger



class DocumentByAssociation(IDocument[Path]):


    def __init__(self, doc_id: Path):
        super().__init__(doc_id)
        self.raw_terms: list[Any] = list(get_word_stream(doc_id))
        self.modified_term_list: list[ITerm] = list(self.transformation(self.raw_terms))

    @property
    def transformation(self):
        return IDsAndStreamsGenerator.stream_overall_transformation

    @property
    def length(self):
        return len(self.modified_term_list)
    def stream_terms(self):
        return self.modified_term_list.__iter__()

    def raw_term_stream(self) -> Iterator[Any]:
        return self.raw_terms.__iter__()


if __name__ == "__main__":
    d = DocumentByAssociation()