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

def handle_query(query: str):
    
    query: Iterator[SITerm] = DIDAndStreamsGenerator.stream_overall_transformation(string_split(query))
    query: list[SITerm] = list(query)
    make_id_scr_pair = lambda did: (
        did, 
        combiner.combine(tfidf.safe_calc_tf_idf(w, did) for w in query) 
        )

    best_docs: list[tuple[DocumentIdentifier, Number]] = heapq.nlargest(
        hm_results,
        (make_id_scr_pair(did) for did in docs.document_ids()),
        key=lambda did_score: did_score[1] #just the score
        )

    # best_docs = sorted((make_id_scr_pair(did) for did in DocumentsHolder().document_ids()), key=lambda p:p[1], reverse=True)
    return best_docs



if __name__ == '__main__':
    #bad inits

    #process
    while True:
        query: str = input("Enter query: ")
        g_logger.info(f"got from user query, \"{query}\"d")
        res: list[tuple[DocumentIdentifier, Number]] = handle_query(query)

        for doc_id, scr in res:
            print(f"document with id {nicify_doc_id(doc_id)} got match {scr}")
        
 
    

