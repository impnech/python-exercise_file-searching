from collections import defaultdict

from Organizing.I_InverseIndex import *
from Organizing.ICorpus import *
from Organizing.NumericTermInfoInDocument import *


class InverseIndexCounter(I_InverseIndex[int]):
    _corpus: ICorpus
    mat: dict[ITerm, dict[DocumentIdentifier, int]]

    def __init__(self, corpus: ICorpus):
        super().__init__(corpus)
        self._corpus = corpus
        self.mat: dict[ITerm, defaultdict[DocumentIdentifier, int]] = defaultdict(lambda: defaultdict(int))
        for d in corpus.values():
            for t in d.get_terms():
                self.mat[t][d.get_id()] += 1

    def update(self, subject: Observable, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        raise NotImplemented("update of inverseindeximp")
        pass

    def __getitem__(self, __key: ITerm) -> Mapping[DocumentIdentifier, int]:
        return self.mat.__getitem__(__key)

    def __len__(self) -> int:
        return len(self.mat)
        pass

    def __iter__(self) -> Iterator[ITerm]:
        return self.mat.__iter__()
