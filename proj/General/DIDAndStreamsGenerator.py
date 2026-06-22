from Parsing.Splitter import file_split
from Parsing.StringStreamTransformer import *
from pathlib import Path
from General.ITerm import  ITerm
from General.DocumentManager import document_paths_and_files_in_dir_map
from functools import reduce

SPath = str | Path
SITerm = str | ITerm


class DIDAndStreamGenerator:
    """
    responsible for the classmethod get_did_string_streams_pairs
    """

    #todo pull from config
    _sample_files_dir_path: SPath = Path(r'../files/sample_texts')

    # todo all this shall be replaces with config
    from Parsing.Lowerizer import Lowerizer;
    from Parsing.NoiseRemover import NoiseRemover; from Parsing.StopwordsRemover import StopwordsRemover
    from Parsing.Termifier import Termifier; from Parsing.BadPatternsRemover import BadPatternsRemover
    transformers_list: list[StringStreamTransformer] = [
        Lowerizer,
        NoiseRemover,
        StopwordsRemover,
        BadPatternsRemover,
        #Termifier
        ]

    @classmethod
    def get_did_string_streams_sample_pairs(cls, d_path: SPath = None) -> Iterator[tuple[SPath, Iterator[ITerm | str]]]:

        d_path = d_path or cls._sample_files_dir_path

        #make sure the list is initialized, from config of course
        transformations: Iterator[Callable[[SITerm], SITerm]] = map(lambda t: t.transform, cls.transformers_list)
        # composition of the transformations
        func: Callable[[Iterator[SITerm]], Iterator[SITerm]] = reduce(lambda acc, f: (lambda x: f(acc(x))), transformations, file_split)
        return document_paths_and_files_in_dir_map(d_path, func)



if __name__ == '__main__':
    print(*DIDAndStreamGenerator.get_did_string_streams_sample_pairs())
    g = DIDAndStreamGenerator.get_did_string_streams_sample_pairs()
    first = next(g)
    print(first[0])
    print(*first[1], sep="#")
