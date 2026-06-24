from abc import abstractmethod, ABC
from typing import *

from General.DictHandler import DictHandler
from General.ITerm import ITerm
from General.InvertedIndex import InvertedIndex, DH
from Building.IDocument import DocumentIdentifier

from General.DIDAndStreamsGenerator import DIDAndStreamsGenerator

class TF(InvertedIndex, ABC):
    @abstractmethod
    def calc_tf(self, term: ITerm, doc_id: DocumentIdentifier) -> float:
        raise NotImplementedError(f"Generic TF doesn't have calculation implementation")

    def reset(self):
        for doc_id, stream in DIDAndStreamsGenerator.get_did_string_streams_sample_pairs():
            
            for term in stream:
                if term not in self._dict_handler: 
                    from General.DictHandlerFactory import DictHandlerFactory
                    self._dict_handler[term] = DictHandlerFactory.get_dict_handler()
                d_term: DH = self._dict_handler[term]
                if doc_id not in d_term:
                    d_term[doc_id] = self.calc_tf(term, doc_id)

if __name__ == '__main__':
    from General.DictHandlerFactory import DictHandlerFactory
    #TF._dict_handler(DictHandlerFactory.get_dict_handler())
    print(TF._dict_handler)
    pass
