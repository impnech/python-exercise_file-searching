from pathlib import Path
from typing import *
from Loggers.g_logging import g_logger
from EnvManager import force_get_env
from Parsing.Splitter import file_split

#todo clean this file


SPath = str | Path



def get_documents(dirpath: str | Path) -> Iterator[TextIO]:
    return map(lambda p: p[1], document_paths_and_files_in_dir_map(dirpath))


def get_document_paths(dirpath: str | Path):
    return map(lambda p: p[0], document_paths_and_files_in_dir_map(dirpath))


# TODO: think, do we really wanna be dependent on a file in Parsing?, maybe delete this,
def get_term_streams(dirpath: str | Path, delim: str = None) -> Iterator[Iterator[str]]:
    g_logger.warning(f"using a function that maybe should be deleted, {get_term_streams.__name__}")

    return map(lambda p: p[1], document_paths_and_files_in_dir_map(dirpath, lambda file: file_split(file, delim)))


def document_paths_and_files_in_dir_map(dirpath: str | Path, func: Callable[[TextIO], Any] = None) -> Iterator[tuple]:
    dirpath = Path(dirpath)
    for file_path in dirpath.iterdir():
        if not file_path.is_file():
            g_logger.warning(f"in {dirpath}, there exit {file_path} which is not file. Only files were expected here")
            continue
        with open(file_path, "r") as file:
            if func is None:
                rv = file
            else:
                rv = func(file)
            yield file_path, rv




def _get_file(file_path: str | Path, func: Callable[[TextIO], Any] = None) -> Iterator[TextIO]:
    raise DeprecationWarning(f"{_get_file.__name__}")

    file_path = Path(file_path)
    with open(file_path) as file:
        yield file


def get_word_stream(file_path: SPath, func=None, delim=None) -> Iterator[str]:

    file_path = Path(file_path)
    with open(file_path) as f:
        for w in file_split(f, delim):
            if func is None:
                yield w
            else: yield func(w)


if __name__ == '__main__':
    
    _dir_path: SPath = Path(force_get_env("DOCUMENTS_PATH"))

    g = get_word_stream(Path())

    exit()
    from Parsing.Lowerizer import Lowerizer
    for p in document_paths_and_files_in_dir_map(_dir_path, lambda x: Lowerizer.transform(file_split(x))):
        print(p)
        print(*p[1], sep="#")
    exit()

if __name__ == '__main__':
    for x in get_documents(_dir_path):
        print(type(x), x.name)
        for line in file_split(x):
            print(line)
