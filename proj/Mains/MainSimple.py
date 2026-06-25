#imports
from typing import *
import re
from Loggers.g_logging import g_logger
from Computing.TF_IDF import *
from General.DIDAndStreamsGenerator import DIDAndStreamsGenerator
from Parsing.Splitter import *
from Computing.CombineNumbers import CombineNumbers
from General.ITerm import ITerm
from esthetic.Document import *
SITerm = str | ITerm
#max heap in python
import heapq


#bad imports
from Computing.TF_IDFMultiply import TF_IDFMultiply
from Computing.PNormCombine import PNormCombine
from Building.DocumentsHolder import *

#inits
docs: DocumentsHolder = DocumentsHolder()

#bad inits
combiner: Type[CombineNumbers] = PNormCombine()
tfidf: TF_IDF = TF_IDFMultiply()

hm_results: int = 3

def nice_print(res):
    for doc_id, scr in res:
            print(f"document {nicify_doc_id(doc_id)} got match {scr}")


test_query = """
language used in web development. : change is one of the most pressing issues of our  :  learning has  revolutionized the deep field of artificial :  Space exploration has advanced  " 
deep 
"""


def handle_query(query: str):

    query: Iterator[SITerm] = DIDAndStreamsGenerator.stream_overall_transformation(string_split(query))
    query: list[SITerm] = list(query)
    make_id_scr_pair = lambda did: (
        did, 
        combiner.combine(tfidf.safe_calc_tf_idf(w, did) for w in query) 
        )
    # with sorted()
    # best_docs = sorted((make_id_scr_pair(did) for did in DocumentsHolder().document_ids()), key=lambda p:p[1], reverse=True)
    # nice_print(best_docs)
    # print('\n\n\n')

    # generally it's better to use heap, for O(n) time instead of O(n*log(n)) of sorting.
    # the extraction of the k first will take k*log(n) and it's reasnable to assume k is small (3 in our case, unlike n, which is a whole 4), 
    # so the whole operation is O(k)
    # (but i'm not going to vouch for python implementaion efficency, sorted() was optimized to death)
    
    # with heapq
    best_docs: list[tuple[DocumentIdentifier, Number]] = heapq.nlargest(
        hm_results,
        (make_id_scr_pair(did) for did in docs.document_ids()),
        key=lambda did_score: did_score[1] #just the score
        )
    nice_print(best_docs)

    return best_docs



if __name__ == '__main__':
    #bad inits

    #process
    while True:
        query: str = input("Enter query: (quitting is still with Ctrl+C)")
        g_logger.info(f"got from user query, \"{query}\"d")
        res: list[tuple[DocumentIdentifier, Number]] = handle_query(query)

        
 
    

