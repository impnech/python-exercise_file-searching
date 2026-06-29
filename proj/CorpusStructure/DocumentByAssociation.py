from CorpusStructure.IDocument import IDocument, ITerm , DocumentIdentifier
from pathlib import Path
from FileUsers.IDsAndStreamsGenerator import IDsAndStreamsGenerator
from Loggers.g_logging import g_logger



class DocumentByAssociation(IDocument[Path]):

    def __init__(self, doc_id: Path):
        super().__init__(doc_id)
        try:
            with open(doc_id) as f:
                self.term_list: list[ITerm] = list(IDsAndStreamsGenerator.stream_overall_transformation_applied_on_file(f))
        except FileNotFoundError as e:
            g_logger.critical(f"can't extract document from {doc_id}")
            g_logger.exception(e)
            raise FileNotFoundError(e)

    @property
    def length(self):
        return len(self.term_list)
    def stream_terms(self):
        return self.term_list.__iter__()


if __name__ == "__main__":
    d= DocumentByAssociation()