
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

    
    def get_all_terms_with_duplicates(self, dpath: SPath = None) -> Iterator[ITerm | str]:
        """
        has alternative in DIDAndStreamsGenerator,
        """        
        for doc_id in self:
            doc: IDocument = self[doc_id]
            for term in doc.stream_terms():
                yield term

if __name__ == '__main__':
    docs = DocumentsHolder()
