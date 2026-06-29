from abc import abstractmethod
from numbers import Number

from CorpusStructure.ITerm import ITerm
from Computing.InvertedIndex import InvertedIndex, DH
from CorpusStructure.IDocument import DocumentIdentifier

# questionalbe imports
from FileUsers.IDsAndStreamsGenerator import IDsAndStreamsGenerator
from Computing.Calculator import Calculator
from Dicts.DictHandlerFactory import DictHandlerFactory
from DesignPatterns.DefaultHolder import DefaultHolder

class TF(InvertedIndex, Calculator, DefaultHolder):


    def __init__(self, default_value=0):
        super().__init__(default_value)

    @abstractmethod
    def calc(self, term: ITerm, doc_id: DocumentIdentifier) -> Number:
        raise NotImplementedError(f"Generic TF doesn't have calculation implementation")

    def safe_calc_tf(self,term: ITerm, doc_id: DocumentIdentifier) -> Number:
        try:
            return self.calc(term, doc_id)
        except KeyError:
            return self.default_value 
            
    def reset(self):
        
        for doc_id, stream in IDsAndStreamsGenerator.get_did_string_streams_sample_pairs():
            
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
