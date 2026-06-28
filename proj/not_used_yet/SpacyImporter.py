#not used
from Loggers.g_logging import g_logger


try:
    import spacy
    nlp = 
except ImportError as e:
    g_logger.error("coudln't import spacy module")
    g_logger.exception(e)
    # g_logger.warning("the LemmatizerSpacy class will be empty, just enough to not crush")
    raise ImportError("couldn't import spacy, this lemmataizer won't work")
    
