from Building.IDocument import DocumentIdentifier, IDocument
from Structure.Observing import *
from abc import *
from typing import *


class ICorpus(Observable, Mapping[DocumentIdentifier, IDocument[DocumentIdentifier]], ABC):
    pass

