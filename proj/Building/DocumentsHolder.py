
from General.DictUsingInfo import DictUsingInfo
from Building.IDocument import *
from typing import *
from General.DIDAndStreamsGenerator import *


# todo from config
from Building.DocumentFactory import DocumentFactory

class DocumentsHolder(DictUsingInfo[DocumentIdentifier, IDocument], Generic[DocumentIdentifier]):
    def document_ids(self) -> Iterator[DocumentIdentifier]:
        return self.__iter__()

    def get_doc_by_id(self, doc_id: DocumentIdentifier) -> IDocument:
        return self._dict_handler[doc_id]
    def reset(self):
        #using here not generic, since
        for doc_id in DIDAndStreamsGenerator.get_docids():
            self._dict_handler[doc_id] = DocumentFactory.get_document(doc_id)




if __name__ == '__main__':
    docs = DocumentsHolder()
