from abc import abstractmethod
from numbers import Number

from Building.ITerm import ITerm
from General.InvertedIndex import InvertedIndex, DH
from Building.IDocument import DocumentIdentifier

# questionalbe imports
from General.DIDAndStreamsGenerator import DIDAndStreamsGenerator
from Computing.Calculator import Calculator
from General.DictHandlerFactory import DictHandlerFactory


class TF(InvertedIndex, Calculator):


    __default_value: Number
    @property
    def default_value(self) -> Number:
        return self.__default_value 
    
    @abstractmethod
    def calc(self, term: ITerm, doc_id: DocumentIdentifier) -> Number:
        raise NotImplementedError(f"Generic TF doesn't have calculation implementation")

    def safe_calc_tf(self,term: ITerm, doc_id: DocumentIdentifier) -> Number:
        try:
            return self.calc(term, doc_id)
        except KeyError:
            return self.default_value 
            
    def reset(self, default_val = 0):
        self.__default_value = default_val
        for doc_id, stream in DIDAndStreamsGenerator.get_did_string_streams_sample_pairs():
            
            for term in stream:
                if term not in self._dict_handler: 
                    self._dict_handler[term] = DictHandlerFactory.get_dict_handler()
                d_term: DH = self._dict_handler[term]
                if doc_id not in d_term:
                    d_term[doc_id] = self.calc(term, doc_id)

if __name__ == '__main__':
    #TF._dict_handler(DictHandlerFactory.get_dict_handler())
    #print(TF._dict_handler)
    pass
