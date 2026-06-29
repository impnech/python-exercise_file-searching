
from CorpusStructure.IDocument import DocumentIdentifier, IDocument
from AppConfig import get_class_implementations_list
from CorpusStructure.ITerm import ITerm

from Loggers.g_logging import g_logger
from EnvManager import force_get_env
from CorpusStructure.ICorpus import ICorpus
from CorpusStructure.DocumentFactory import DocumentFactory


g_logger.info(f"{__file__} bing imported")
SITerm = str | ITerm

# wish to avoid

from pathlib import Path
from Parsing.StringStreamTransformer import *
from FileUsers.FileManager import get_word_stream, get_document_paths


SPath = str | Path


class StateLessCorpusByPath(ICorpus):
    """
    (bad name, will be changed, with pycharm)
    used knowing that ITerm is string-like
    and IDocument is path-like
    """

    @classmethod
    def get_document(cls, doc_id: DocumentIdentifier) -> IDocument:
        return DocumentFactory.get_document_implementation(doc_id)

    _sample_files_dir_path: SPath = force_get_env("DOCUMENTS_PATH")

    transformers_list: list[StringStreamTransformer] = get_class_implementations_list(StringStreamTransformer.__name__)


    @classmethod
    def _definitely_path(cls, d_path: SPath | None) -> Path:
        return d_path or cls._sample_files_dir_path

    @classmethod
    def get_doc_ids(cls, dpath: SPath = None):
        dpath = cls._definitely_path(dpath)
        return get_document_paths(dpath)


if __name__ == '__main__':

    g = StateLessCorpusByPath.id_and_stream_pairs()

    first = next(g)
    print(first[0])
    print(*first[1], sep="#")
