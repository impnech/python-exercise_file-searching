from CorpusStructure.IDocument import DocumentIdentifier, IDocument
from DesignPatterns.Observing import *
from abc import *
from typing import *


class ICorpus(Observable, Mapping[DocumentIdentifier, IDocument[DocumentIdentifier]], ABC):
    pass

