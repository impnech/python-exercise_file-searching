from pathlib import Path
from typing import *
from Loggers.g_logging import g_logger
from Parsing.Splitter import file_split

# TODO take the path from config
_dir_path: str | Path = Path(r"..\files\sample_texts")


def get_documents(dirpath: str | Path = _dir_path) -> Iterator[TextIO]:
    return __files_in_dir_map(dirpath)


# TODO: think, do we really wanna be dependent on a file in Parsing?, probably delete this,
def get_term_streams(dirpath: str | Path = _dir_path) -> Iterator[str]:
    g_logger.warning(f"using a function that maybe should be deleted, {get_term_streams.__name__}")
    return __files_in_dir_map(dirpath, file_split)


def __files_in_dir_map(dirpath: str | Path = _dir_path, func: Callable[[TextIO], Any] = None) -> Iterator:
    dirpath = Path(dirpath)
    for file_path in dirpath.iterdir():
        if not file_path.is_file():
            g_logger.warning(f"in {dirpath}, there exit {file_path} which is not file. Only files were expected here")
            continue
        with open(file_path, "r") as file:
            if func is None:
                yield file
            else:
                yield func(file)


_stop_words_file_path: str | Path = Path(r"..\files\stopwords.txt")


def get_file(file_path: str | Path):
    file_path = Path(file_path)
    with open(file_path) as file:
        yield file


if __name__ == '__main__':
    for x in get_documents():
        print(type(x), x.name)
        for line in file_split(x):
            print(line)
