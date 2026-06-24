from abc import abstractmethod

from Building.IDocument import DocumentIdentifier
from Computing.TF import TF
from Computing.IDF import IDF
from General import ITerm
from General.ICorpusInfo import ICorpusInfo
from Loggers.g_logging import g_logger

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
    def calc_tf_idf(self, term: ITerm, doc_id: DocumentIdentifier) -> float:
        raise NotImplementedError(f"technically, there are more than one variant of tf_idf calculation")