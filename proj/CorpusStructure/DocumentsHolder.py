from typing import Iterator

from InfoLogic.DictUsingInfo import DictUsingInfo
from CorpusStructure.IDocument import IDocument, DocumentIdentifier

#from FileUsers.StateLessCorpusByPath import *
from FileUsers.StateLessCorpusByPath import StateLessCorpusByPath

from CorpusStructure.ICorpus import ITerm
from CorpusStructure.DocumentFactory import DocumentFactory


class DocumentsHolder(DictUsingInfo[DocumentIdentifier, IDocument],):
    def get_doc_ids(self) -> Iterator[DocumentIdentifier]:
        """used just by self"""
        return self.__iter__()

    def get_document(self, doc_id: DocumentIdentifier) -> IDocument:

        return self._dict_handler[doc_id]
    
    def reset(self):
        for doc_id in StateLessCorpusByPath.get_doc_ids():
            self._dict_handler[doc_id] = DocumentFactory.get_document_implementation(doc_id)

    
    def all_terms(self) -> Iterator[ITerm | str]:
        """
        has alternative in StateLessCorpusByPath,
        """
        for doc_id in self.get_doc_ids():
            doc: IDocument = self[doc_id]
            for term in doc.stream_terms():
                yield term

if __name__ == '__main__':
    pass
    #docs = DocumentsHolder()
