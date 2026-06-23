from General.DictUsingInfo import DictUsingInfo
from Building.IDocument import *
from typing import *
from General.DIDAndStreamsGenerator import *


#DocumentInfo = TypeVar('DocumentInfo')


class DocumentsHolder(DictUsingInfo[DocumentIdentifier, IDocument], Generic[DocumentIdentifier]):
    def document_ids(self) -> Iterator[DocumentIdentifier]:
        return self.__iter__()

    def reset(self):
        #using here not generic, since
        for doc_id in DIDAndStreamsGenerator.get_docids():
            self._dict_handler[doc_id] = IDocument(doc_id)




if __name__ == '__main__':
    docs = DocumentsHolder()
