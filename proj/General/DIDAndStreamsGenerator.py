#from markdown_it.rules_core import inline

from Parsing.Splitter import file_split
from Parsing.StringStreamTransformer import *
from pathlib import Path
import importlib
from AppConfig import force_get_setting, get_class_implementations_list
from General.ITerm import ITerm
from General.DocumentManager import document_paths_and_files_in_dir_map
from General.DocumentManager import *
from functools import reduce
from Loggers.g_logging import g_logger
import os
from EnvManager import force_get_env



g_logger.info(f"{__file__} bing imported")
SPath = str | Path
SITerm = str | ITerm


class DIDAndStreamsGenerator:
    """
    (bad name, will be changed, with pycharm)
    responsible for the classmethod get_did_string_streams_pairs
    """


    _sample_files_dir_path: SPath = force_get_env("DOCUMENTS_PATH")

    transformers_list: list[StringStreamTransformer] = get_class_implementations_list(StringStreamTransformer.__name__)

    stream_overall_transformation: Callable[[Iterator[SITerm]], Iterator[SITerm]]
    try:
        stream_overall_transformation
    except (AttributeError, NameError):
        # make sure the list is initialized, from config of course
        _transformations: Iterator[Callable[[SITerm], SITerm]] = map(lambda t: t.transform, transformers_list)
        # composition of the transformations
        stream_overall_transformation: Callable[[Iterator[SITerm]], Iterator[SITerm]] = reduce(
            lambda acc, f: (lambda s: f(acc(s))),
            _transformations,
        )

    @classmethod
    def stream_overall_transformation_applied_on_file(cls,some_file):
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
        has alternative in DocumentsHolder, but this one is more efficient, since it doesn't need to hold the documents in memory
        """
        for _, stream in cls.get_did_string_streams_sample_pairs(dpath):
            for term in stream:
                yield term

if __name__ == '__main__':

    g = DIDAndStreamsGenerator.get_docids()
    for x in g: print(x)


    g = DIDAndStreamsGenerator.get_did_string_streams_sample_pairs()

    first = next(g)
    print(first[0])
    print(*first[1], sep="#")
