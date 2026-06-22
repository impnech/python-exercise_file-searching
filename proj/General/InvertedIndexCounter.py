from InvertedIndex import *
from Building.IDocument import DocumentIdentifier
from DictHandler import *
from DIDAndStreamsGenerator import DIDAndStreamGenerator
from get_sample_files import get_did_string_streams_sample_pairs

#todo better factory
from DictHandlerFactory import *

DH = TypeVar("DH", bound=DictHandler)

_Map = Mapping[DocumentIdentifier, int]


class InvertedIndexCounter(InvertedIndex[_Map], Generic[DH, DocumentIdentifier]):
    """
    when will need to use this static class, it's "interface" can be InvertedIndex[Mapping[DocumentIdentifier,int]]
    In order for this inverted index to hold information, there's need to call the class-method, init(cls)
    """


    _dict_handler: DH


    @classmethod
    def init(cls, dh: DH):
        cls._dict_handler: DH = dh
        cls.reset()
    @classmethod
    def reset(cls):
        #cls._dict_handler = DictHandlerFactory.get_dict_handler()
        #todo, it's supposed to be ITerms
        for did, stream in DIDAndStreamGenerator.get_did_string_streams_sample_pairs():
            for word in stream:
                if word not in cls._dict_handler:
                    cls._dict_handler[word] = DictHandlerFactory.get_dict_handler()
                if did not in cls._dict_handler[word]:
                    cls._dict_handler[word][did] = 1
                else: cls._dict_handler[word][did] += 1


    @classmethod
    def __len__(cls):
        return cls._dict_handler.__len__()

    @classmethod
    def __iter__(cls) -> Iterator[ITerm]:
        return cls._dict_handler.__iter__()
    @classmethod
    def __getitem__(cls, key: ITerm) -> _Map:
        return cls._dict_handler.__getitem__(key)


if __name__ == '__main__':
    inv = InvertedIndexCounter()
    from SimpleDictHandler import SimpleDictHandler
    InvertedIndexCounter.init(SimpleDictHandler())
    for x in inv.items(): print(f"{x[0]}: {x[1]}")
    print(len(inv))
