from FileUsers.FileManager import get_documents, get_term_streams, document_paths_and_files_in_dir_map
from pathlib import Path
from EnvManager import force_get_env
from Parsing.Splitter import file_split

# TOthink maybe use this file

_sample_file_dir_path: str | Path = force_get_env("DOCUMENTS_PATH")


def get_sample_files():
    return get_documents(_sample_file_dir_path)


def get_sample_word_streams(delim: str = None):
    raise NotImplementedError()
    return get_term_streams(_sample_file_dir_path, delim)


def get_did_string_streams_sample_pairs():
    return document_paths_and_files_in_dir_map(_sample_file_dir_path, file_split)


if __name__ == '__main__':
    for p in get_did_string_streams_sample_pairs():
        print(p)
        for w in p[1]:
            print(w, end="#")
        print()


