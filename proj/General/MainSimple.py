from typing import *
from Computing.TF_IDF import *
from General.DIDAndStreamsGenerator import DIDAndStreamsGenerator

from General.ITerm import ITerm
SITerm = str | ITerm


#bad imports
from Computing.TF_IDFMultiply import TF_IDFMultiply


if __name__ == '__main__':
    pass
    if 1==1:
        query: str = "One_trasf,sdf ssfkje;sdf  'sdf sse'fs  sdsf DSFS sdfsds" #input("Enter query: ")
        #query: Iterator[ITerm | str] = DIDAndStreamsGenerator.stream_overall_transformation(query)
        query: Iterator[SITerm] = DIDAndStreamsGenerator.stream_overall_transformation(query)
        li_query = [str(term) for term in query]
        print(f"query: {li_query}")



