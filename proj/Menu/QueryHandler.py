from typing import Iterator

from AppConfig import get_class_implementation, get_default_value, get_class_implementation_instance
from Computing.Calculator import Calculator
from Computing.CombineNumbers import CombineNumbers
from FileUsers.IDsAndStreamsGenerator import IDsAndStreamsGenerator, SITerm
from Menu.GetNBest import GetNBest
from Parsing.Splitter import string_split
from esthetic.Document import nicify_doc_id

#inits
combiner: CombineNumbers = get_class_implementation_instance(CombineNumbers.__name__)
calculator: Calculator = get_class_implementation(Calculator.__name__)()
selector: type[GetNBest] = get_class_implementation(GetNBest.__name__)

hm_results: int = get_default_value("how_many_results_to_show")

def nice_print(_iter):
    for doc_id, scr in _iter:
        print(f"document {nicify_doc_id(doc_id)} got match {scr}")

def handle_query(query: str):
    query: Iterator[SITerm] = IDsAndStreamsGenerator.stream_overall_transformation(string_split(query))
    query: list[SITerm] = list(query)

    score_by = lambda did: combiner.combine((calculator.calc(w, did) for w in query))

    best_docs = selector.gen_n_best_with_score(hm_results, IDsAndStreamsGenerator.get_docids(), score_by)
    nice_print(best_docs)
    return best_docs


if __name__ == '__main__':
    qr = "if i could believe to be"
    handle_query(qr)

