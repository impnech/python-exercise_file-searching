from abc import abstractmethod

from Building.IDocument import DocumentIdentifier
from Computing.TF import TF
from Computing.IDF import IDF
from General import ITerm
from General.ICorpusInfo import ICorpusInfo
from Loggers.g_logging import g_logger
from numbers import Number

# bad imports. todo this from config
from Computing.TFdivBySum import TFdivBySum
from Computing.SimpleLogorithmicIDF import SimpleLogorithmicIDF


class TF_IDF(ICorpusInfo):
    """
    at least the general case of tf-idf, which is tf(t,d)*idf(t,D), isn't worthy of storing it's computation
    so, no inheretince from DictUsingInfo
    """

    tf: TF = TFdivBySum()
    idf: IDF = SimpleLogorithmicIDF()
    
    def reset(self):
        self.tf.reset()
        self.idf.reset()


    @abstractmethod
    def calc_from_numbers(self,tf: Number, idf: Number) -> Number:
        raise NotImplementedError(f"technically, there are more than one variant of tf_idf calculation")


    def calc_tf_idf(self, term: ITerm, doc_id: DocumentIdentifier) -> Number:
        return self.calc_from_numbers(self.tf.calc_tf(term, doc_id),self.idf.calc_idf(term))
    
    def safe_calc_tf_idf(self, term: ITerm, doc_id: DocumentIdentifier) -> Number:
        """
        for when the term possible doesn't exist in any document.
        """
        return self.calc_from_numbers(self.tf.safe_calc_tf(term, doc_id),self.idf.safe_calc_idf(term))

        