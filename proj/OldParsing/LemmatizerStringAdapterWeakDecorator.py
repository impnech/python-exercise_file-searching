from abc import ABC
# TODO: import spacy, or nltk maybe the choice is from config
from StringAdapterWeakDecorator import *


class LemmatizerStringAdapterWeakDecorator(StringAdapterWeakDecorator):
    def __init__(self, component: IStringAdapter) -> None:
        super().__init__(component)
        self.__lemmatized_value = None
        raise NotImplemented("lemmatization")
        # TODO: import lemmatization and use it

    @property
    def _value(self) -> str:
        return self.__lemmatized_value
        pass
