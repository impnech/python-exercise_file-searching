from Building.CorpusInfo import *
from Building.IDocument import *
from typing import *


DocumentInfo = TypeVar('DocumentInfo')


class DocumentsInfo(ICorpusInfo, Generic[DocumentIdentifier, DocumentInfo], Mapping[DocumentIdentifier, DocumentInfo], ABC):
    pass


