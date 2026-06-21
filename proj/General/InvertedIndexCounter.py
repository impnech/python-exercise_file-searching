from InvertedIndex import *
from Building.IDocument import DocumentIdentifier
from DictHandler import *

DH = TypeVar("DH", bound=DictHandler)

_Map = Mapping[DocumentIdentifier, int]


class InvertedIndexCounter(InvertedIndex[_Map], Generic[DH, DocumentIdentifier]):
    """
    when will need to use this static class, it's "interface" can be InvertedIndex[Mapping[DocumentIdentifier,int]]
    In order for this inverted index to hold information, there's need to call the class-method, init(cls)
    """

    # TODO the choosing from config
    from SimpleDictHandler import SimpleDictHandler
    _dict_handler: DH = SimpleDictHandler()


    @classmethod
    def init(cls):
        cls.reset()
    @staticmethod
    def reset():
        raise NotImplemented()



    def __len__(cls):
        pass

    def __iter__(self) -> Iterator[ITerm]:
        pass
        __len__ = _dict_handler.__len__
        __iter__ = _dict_handler.__iter__
        __getitem__ = _dict_handler.__getitem__

    def __getitem__(self, key: ITerm) -> _Map:
        pass


if __name__ == '__main__':
    inv = InvertedIndexCounter()
    InvertedIndexCounter.reset()