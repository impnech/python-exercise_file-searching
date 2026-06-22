from DictHandler import *
from SimpleDictHandler import *
from ShelveDictHandler import *


# todo better (config)
class DictHandlerFactory:
    @staticmethod
    def get_dict_handler():
        return SimpleDictHandler()
