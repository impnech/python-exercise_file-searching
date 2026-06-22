
from DictHandler import *


class SimpleDictHandler(DictHandler):

    def __init__(self) -> None:
        self.__actual_dict: dict[KT, VT] = {}


    def __setitem__(self, key: KT, value: VT) -> None:
        self.__actual_dict[key] = value

    def __getitem__(self, __key: KT) -> VT:
        return self.__actual_dict[__key]

    def __len__(self) -> int:
        return self.__actual_dict.__len__()

    def __iter__(self) -> Iterator[KT]:
        return self.__actual_dict.__iter__()

    def __str__(self):
        return self.__actual_dict.__str__()


if __name__ == '__main__':
    d: SimpleDictHandler[int, str] = SimpleDictHandler[int, str]()
    d[3] = "ASd"
    d[3.5] = quit
    print(d[3])
    print(1 in d)


