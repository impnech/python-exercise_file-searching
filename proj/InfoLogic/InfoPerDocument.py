from InfoLogic.DictUsingInfo import DictUsingInfo, VT

from CorpusStructure.IDocument import DocumentIdentifier
from typing import Generic

class InfoPerDocument(DictUsingInfo[DocumentIdentifier, VT], Generic[DocumentIdentifier, VT]):
    pass

if __name__ == '__main__':
    pass # say = InfoPerDocument()




