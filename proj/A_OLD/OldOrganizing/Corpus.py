from ICorpus import *


class Corpus(ICorpus):
    def __init__(self, documents: Iterable[IDocument[DocumentIdentifier]]):
        super().__init__()
        self._documents: dict[DocumentIdentifier, IDocument[DocumentIdentifier]] = {}
        for doc in documents:
            did: DocumentIdentifier = doc.doc_id()
            if did in doc:
                # TODO logging error
                raise KeyError(f"document_id {did} exist in {documents} more than once, ids are supposed to be unique")
            self._documents[did] = doc

    def __len__(self):
        return len(self._documents)

    def __iter__(self) -> Iterator[DocumentIdentifier]:
        return self._documents.__iter__()

    def __getitem__(self, __key: DocumentIdentifier) -> IDocument:
        return self._documents.__getitem__(__key)
