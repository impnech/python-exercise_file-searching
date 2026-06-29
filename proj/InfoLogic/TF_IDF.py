from abc import abstractmethod

from AppConfig import get_class_implementation, get_class_implementation_instance

from CorpusStructure.IDocument import DocumentIdentifier
from InfoLogic.Calculator import Calculator
#from InfoLogic.Calculator import Calculator
from InfoLogic.TF import TF
from InfoLogic.IDF import IDF
from CorpusStructure import ITerm
from numbers import Number


class TF_IDF(Calculator):
    """
    at least the general case of tf-idf, which is tf(t,d)*idf(t,D), isn't worthy of storing it's computation
    so, no inheretince from DictUsingInfo
    """

    tf: TF = get_class_implementation_instance(TF.__name__)
    idf: IDF = get_class_implementation_instance(IDF.__name__)
    
    def reset(self):
        self.tf.reset()
        self.idf.reset()


    @abstractmethod
    def calc_from_numbers(self,tf: Number, idf: Number) -> Number:
        raise NotImplementedError(f"technically, there are more than one variant of tf_idf calculation")


    def unsafe_calc(self, term: ITerm, doc_id: DocumentIdentifier) -> Number:
        return self.calc_from_numbers(self.tf.calc(term, doc_id),self.idf.calc_idf(term))
    
    def calc(self, term: ITerm, doc_id: DocumentIdentifier) -> Number:
        """
        for when the term possible doesn't exist in any document.

        """
        return self.calc_from_numbers(self.tf.safe_calc_tf(term, doc_id),self.idf.safe_calc_idf(term))
    
