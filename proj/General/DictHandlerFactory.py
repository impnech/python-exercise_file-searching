from General.DictHandler import *
from General.SimpleDictHandler import *
from General.ShelveDictHandler import *


# todo better (config)
class DictHandlerFactory:
    @staticmethod
    def get_dict_handler():
        return SimpleDictHandler()


        return ShelveDictHandler()
