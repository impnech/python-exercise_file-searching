from A_OLD.OldOrganizing.I_InverseIndex import *
from A_OLD.OldOrganizing.ICorpus import *
from TermCounterInDocument import *


class InverseIndexCounter(I_InverseIndex[TermCounterInDocument]):

    def __init__(self, corpus: ICorpus):
        super().__init__(corpus)
        self.__init_corpus(corpus)

    def __init_corpus(self, corpus: ICorpus):
        self._corpus: ICorpus = corpus
        self.mat: dict[ITerm, dict[DocumentIdentifier, TermCounterInDocument]] = defaultdict(
            lambda: defaultdict(lambda: TermCounterInDocument()))
        for d in corpus.values():
            for t in d.stream_terms():
                self.mat[t][d.doc_id()] += 1

    def update(self, subject: ICorpus, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        if not args and not kwargs:
            self.__init_corpus(subject)
            return
        raise NotImplemented(f"doesn't support currently options {args} and {kwargs}")

    def __getitem__(self, __key: ITerm) -> Mapping[DocumentIdentifier, TermCounterInDocument]:
        return self.mat.__getitem__(__key)

    def __len__(self) -> int:
        return len(self.mat)
        pass

    def __iter__(self) -> Iterator[ITerm]:
        return self.mat.__iter__()


if __name__ == '__main__':
    from Corpus import Corpus
    from Building.DocumentByPath import *
    from General.StringTerm import *

    d1 = DocumentByPath[int](1, ["hello", " there", "my", "", "hello"])
    d2 = DocumentByPath(2, (StringTerm(x) for x in ["hi", " there", "people", "", "hello"]))



    print(type(int),
          type(4),
          type(DocumentIdentifier),
          sep='\n')

    iden3: str = d2.doc_id()
    inv = InverseIndexCounter(Corpus([d1, d2]))

    print(inv[StringTerm("hello")][2])
    print(type(inv["hello"]))
    print(inv["hello"][1])
