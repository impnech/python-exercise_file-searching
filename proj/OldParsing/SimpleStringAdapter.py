from AssociativeStringAdapter import *


class SimpleStringAdapter(AssociativeStringAdapter):
    def __init__(self, val):
        self._value = val

    @property
    def _value(self):
        return self.__value
    @_value.setter
    def _value(self, value):
        self.__value = value
