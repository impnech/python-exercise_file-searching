from Parsing.StringStreamTransformer import *
from AppConfig import get_class_implementations_list, get_class_implementation
from CorpusStructure.ITerm import ITerm
from FileUsers.FileManager import *
from functools import reduce
from Loggers.g_logging import g_logger
from EnvManager import force_get_env

from Parsing.Termifier import Termifier

g_logger.info(f"{__file__} bing imported")
SPath = str | Path
SITerm = str | ITerm


class IDsAndStreamsGenerator:
    """
    (bad name, will be changed, with pycharm)
    used knowing that ITerm is string-like
    and IDocument is path-like
    """


    _sample_files_dir_path: SPath = force_get_env("DOCUMENTS_PATH")

    transformers_list: list[StringStreamTransformer] = get_class_implementations_list(StringStreamTransformer.__name__)

    @classmethod
    def stream_overall_transformation(cls, iterator):
        res = iterator
        for transformer in cls.transformers_list:
            res = transformer.transform(res)
        return res

    @classmethod
    def stream_overall_transformation_applied_on_file(cls, some_file):
        return cls.stream_overall_transformation(file_split(some_file))
    
    @classmethod
    def definitely_path(cls, d_path: SPath | None) -> Path:
        return d_path or cls._sample_files_dir_path

    @classmethod
    def get_did_string_streams_sample_pairs(cls, d_path: SPath = None) -> Iterator[tuple[SPath, Iterator[ITerm | str]]]:

        d_path = cls.definitely_path(d_path)

        return document_paths_and_files_in_dir_map(d_path, cls.stream_overall_transformation_applied_on_file)

    @classmethod
    def get_docids(cls, dpath: SPath = None):
        dpath = cls.definitely_path(dpath)
        return get_document_paths(dpath)

    @classmethod
    def all_terms_with_duplicates(cls, dpath: SPath = None) -> Iterator[ITerm | str]:
        """
        has alternative in DocumentsHolder, but this one is more efficient, since it doesn't need to hold the documents in dict_handler
        """
        for _, stream in cls.get_did_string_streams_sample_pairs(dpath):
            for term in stream:
                yield term

if __name__ == '__main__':

    g = IDsAndStreamsGenerator.get_docids()
    for x in g: print(x)


    g = IDsAndStreamsGenerator.get_did_string_streams_sample_pairs()

    first = next(g)
    print(first[0])
    print(*first[1], sep="#")
