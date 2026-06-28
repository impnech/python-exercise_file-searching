from Parsing.Lemmatizer import Lemmatizer
from Loggers.g_logging import g_logger
from AppConfig import get_outside_variable


try:
    import spacy
except ImportError as e:
    ermsg= "coudln't import spacy module, try 'pip install spacy'"
    g_logger.error(ermsg)
    g_logger.exception(e)
    # g_logger.warning("the LemmatizerSpacy class will be empty, just enough to not crush")
    raise ImportError(ermsg)
    


class LemmatizerSpacy(Lemmatizer):
    try: 
        _lang_model: str = get_outside_variable("language_model") 
        nlp = spacy.load(_lang_model)
    except (ImportError, OSError ) as e:
        g_logger.error(f"didn't find model {_lang_model}, maybe try running on terminal: 'python spacy -m download {_lang_model}'")
        raise ImportError(e)

    @classmethod
    def _str_transform(cls, o_string):
        doc = cls.nlp(o_string)
        tok = doc[0]
        return tok.lemma_ # the human readable lemma
    


if __name__ == "__main__":
    text = "I am running in the park with my dogs deeping, developing my development"

    l = LemmatizerSpacy()
    x = l.transform(text.split())
    print(*x)