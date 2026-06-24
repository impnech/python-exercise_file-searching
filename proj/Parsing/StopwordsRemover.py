from Parsing.BadWordsRemover import *
from pathlib import Path
from General.DocumentManager import get_word_stream


# shouldn't really be static
class StopwordsRemover(BadWordsRemover):

    @classmethod
    def transform(cls, original: Iterator[str] | Iterable[str]) -> Iterator[str]:
        badwords = cls._badwords()
        return filter(lambda w: w not in badwords, original)

    # TODO : take it from .env
    _stop_words_file_path: str | Path = Path(__file__).resolve().parent.parent / Path(r"files\stopwords.txt")
    @classmethod
    def _init_wordset(cls, *args, **kwargs) -> None:
        """
        always initializes to have the file with stopwords,
        will ignore any other parameter
        """
        cls._wordset: set[str] = set(get_word_stream(cls._stop_words_file_path))




if __name__ == '__main__':
    pass


    #StopWordRemover._stopwords()
    #exit()
    #from General.DocumentManager import _get_file, _stop_words_file_path

