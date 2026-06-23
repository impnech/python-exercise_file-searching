from General.DictUsingInfo import DictUsingInfo, VT

from Building.IDocument import IDocument, DocumentIdentifier
from typing import Generic

class InfoPerDocument(DictUsingInfo[DocumentIdentifier, VT], Generic[DocumentIdentifier, VT]):
    pass

if __name__ == '__main__':
    pass # say = InfoPerDocument()




