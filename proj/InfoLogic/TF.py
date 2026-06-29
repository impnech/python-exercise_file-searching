from abc import abstractmethod
from numbers import Number
from AppConfig import get_class_implementation
from CorpusStructure.ITerm import ITerm
from InfoLogic.InvertedIndex import InvertedIndex, DH
from CorpusStructure.IDocument import DocumentIdentifier

# questionalbe imports
#from FileUsers.StateLessCorpusByPath import StateLessCorpusByPath
#from FileUsers.StateLessCorpusByPath import StateLessCorpusByPath

from CorpusStructure.ICorpus import ICorpus
from InfoLogic.Calculator import Calculator
from Dicts.DictHandlerFactory import DictHandlerFactory
from DesignPatterns.DefaultHolder import DefaultHolder

corpus: type[ICorpus] = get_class_implementation(ICorpus)
class TF(InvertedIndex, Calculator, DefaultHolder):


    def __init__(self, default_value=0):
        super().__init__(default_value)


    def calc(self, term: ITerm, doc_id: DocumentIdentifier) -> Number:
        try:
            return self[term][doc_id]
        except KeyError:
            return self.calc_for_new(term,doc_id)
    @abstractmethod
    def calc_for_new(self,term,doc_id):
        raise NotImplementedError("")
    def safe_calc_tf(self, term: ITerm, doc_id: DocumentIdentifier) -> Number:
        try:
            return self.calc(term, doc_id)
        except KeyError:
            return self.default_value 
            
    def reset(self):
        for doc_id, stream in corpus.id_and_stream_pairs():
            for term in stream:
                if term not in self._dict_handler: 
                    self._dict_handler[term] = DictHandlerFactory.get_dict_handler()
                d_term: DH = self._dict_handler[term]
                if doc_id not in d_term:
                    d_term[doc_id] = self.calc(term, doc_id)
        return self

if __name__ == '__main__':
    #TF._dict_handler(DictHandlerFactory.get_dict_handler())
    #print(TF._dict_handler)
    pass
