from General.DocumentManager import get_documents, get_term_streams, document_paths_and_files_in_dir_map
from pathlib import Path

from Parsing.Splitter import file_split

# TODO take the path from config
_sample_file_dir_path: str | Path = Path(r"..\files\sample_texts")


def get_sample_files():
    return get_documents(_sample_file_dir_path)


def get_sample_word_streams(delim: str = None):
    return get_term_streams(_sample_file_dir_path, delim)


def get_did_string_streams_sample_pairs():
    return document_paths_and_files_in_dir_map(_sample_file_dir_path, file_split)


if __name__ == '__main__':
    for p in get_did_string_streams_sample_pairs():
        print(p)
        for w in p[1]:
            print(w, end="#")
        print()

    exit()
    for s in get_sample_word_streams():
        print(s)
        for w in s:
            print(w, end='@')
        print()

