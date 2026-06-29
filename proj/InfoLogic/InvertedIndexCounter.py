from InfoLogic.InvertedIndex import *
from CorpusStructure.IDocument import DocumentIdentifier
from FileUsers.IDsAndStreamsGenerator import IDsAndStreamsGenerator
from InfoLogic.TF import TF

# towantdo better factory
from Dicts.DictHandlerFactory import *

_Map = Mapping[DocumentIdentifier, int]


class InvertedIndexCounter(TF[_Map], Generic[DocumentIdentifier]):
    """
    Although it is a valid implementation for a TF variant, (according to wikipedia at least), it's main use is as an entity of it's own.
    That's why, when will need to use this static class, it's "interface" can be InvertedIndex[Mapping[DocumentIdentifier,int]]
    In order for this inverted index to hold information, there's need to call the class-method, init(cls)
    """

    def reset(self):
        # todo, it's supposed to be ITerms
        for did, stream in IDsAndStreamsGenerator.id_and_stream_pairs():
            for word in stream:
                if word not in self._dict_handler:
                    # remember that this is not nice
                    self._dict_handler[word] = DictHandlerFactory.get_dict_handler()
                if did not in self._dict_handler[word]:
                    self._dict_handler[word][did] = 1
                else:
                    self._dict_handler[word][did] += 1

    def calc(self, term: ITerm, doc_id: DocumentIdentifier):
        try:
            return self[term][doc_id]
        except KeyError:
            return 0 # meaning that term isn't in doc_id, maybe even term isn't at all known


if __name__ == '__main__':
    inv = InvertedIndexCounter()
    inv2 = InvertedIndexCounter()
    print(f"{id(inv)==id(inv2)}")
    for x in inv.items(): print(f"{x[0]}: {x[1]}")
    for x in InvertedIndexCounter().items(): print(f"{x[0]}: {x[1]}")
