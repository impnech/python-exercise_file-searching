from General.MapHandler import *


class DictHandler(MapHandler):
    @abstractmethod
    def __setitem__(self, key: KT, value: VT):
        pass
