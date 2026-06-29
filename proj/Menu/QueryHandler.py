from typing import Iterator

from AppConfig import get_class_implementation, get_default_value, get_class_implementation_instance
from CorpusStructure.ITerm import ITerm
from InfoLogic.Calculator import Calculator
from InfoLogic.CombineNumbers import CombineNumbers
from Menu.GetNBest import GetNBest
from esthetic.Document import nicify_doc_id

#wish to avoid
#from FileUsers.StateLessCorpusByPath import StateLessCorpusByPath
from CorpusStructure.ICorpus import ICorpus
from Parsing.Splitter import string_split
from CorpusStructure.TermifierToStringTerm import TermifierToStringTerm

#inits
corpus: type[ICorpus] = get_class_implementation(ICorpus.__name__)
combiner: CombineNumbers = get_class_implementation_instance(CombineNumbers.__name__)
calculator: Calculator = get_class_implementation(Calculator.__name__)()
selector: type[GetNBest] = get_class_implementation(GetNBest.__name__)


hm_results: int = get_default_value("how_many_results_to_show")

def nice_print(_iter):
    for doc_id, scr in _iter:
        print(f"document {nicify_doc_id(doc_id)} got match {scr}")

def handle_query(query: str):
    query: Iterator[ITerm] = TermifierToStringTerm.termify(string_split(query))
    query: list[ITerm] = list(query)

    score_by = lambda did: combiner.combine((calculator.calc(w, did) for w in query))

    best_docs = selector.gen_n_best_with_score(hm_results, corpus.get_doc_ids(), score_by)
    nice_print(best_docs)
    return best_docs


if __name__ == '__main__':
    qr = "if i could believe to be"
    handle_query(qr)

