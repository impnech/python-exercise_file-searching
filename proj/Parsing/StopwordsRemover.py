from Parsing.BadWordsRemover import *
from pathlib import Path
from General.DocumentManager import _get_word_stream


# shouldn't really be static
class StopwordsRemover(BadWordsRemover):

    @classmethod
    def transform(cls, original: Iterator[str] | Iterable[str]) -> Iterator[str]:
        badwords = cls._badwords()
        return filter(lambda w: w not in badwords, original)

    # TODO : take it from .env
    _stop_words_file_path: str | Path = Path(r"..\files\stopwords.txt")
    @classmethod
    def _init_wordset(cls) -> None:
        cls._wordset: set[str] = set(_get_word_stream(cls._stop_words_file_path))




if __name__ == '__main__':
    #StopWordRemover._stopwords()
    #exit()
    #from General.DocumentManager import _get_file, _stop_words_file_path


    f = next(g)
    print(f.read())
    exit()
    for f in get_stop_words():
        print(f.read(2))
        for l in f:
            print(l)
    exit()
    for f in get_documents():
        for l in f:
            print(l)
    for st in get_term_streams():
        for w in st:
            print(w)
