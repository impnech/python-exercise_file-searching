
from General.DictHandler import *


class SimpleDictHandler(DictHandler):

    def __init__(self) -> None:
        self._actual_dict: dict[KT, VT] = {}

    def __setitem__(self, key: KT, value: VT) -> None:
        self._actual_dict[key] = value

    def __getitem__(self, _key: KT) -> VT:
        return self._actual_dict[_key]

    def __len__(self) -> int:
        return self._actual_dict.__len__()

    def __iter__(self) -> Iterator[KT]:
        return self._actual_dict.__iter__()

    def __str__(self):
        return self._actual_dict.__str__()


if __name__ == '__main__':
    d: SimpleDictHandler[int, str] = SimpleDictHandler[int, str]()
    d[3] = "ASd"
    d[3.5] = quit
    print(d[3])
    print(1 in d)


