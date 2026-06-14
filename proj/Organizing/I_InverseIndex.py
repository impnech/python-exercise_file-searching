import typing
from abc import ABC

from ITerm import *
from IDocument import *
from TermInfoInDocument import *
from Observing import *
from abc import *
from typing import *

T = typing.TypeVar('T', bound=TermInfoInDocument)


class I_InverseIndex(Observer, Mapping[ITerm, Mapping[DocumentIdentifier, T]], ABC):
    """
    Need to implement the 'update' of Observer
    """
    def get_info4term_in_document(self, term: ITerm, doc_id: DocumentIdentifier) -> T:
        return self[term][doc_id]

