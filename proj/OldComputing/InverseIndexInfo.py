from OldOrganizing.ICorpus import *
from OldOrganizing.I_InverseIndex import *
from OldOrganizing.NumericTermInfoInDocument import *


class InverseIndexInfo:
    _inverse_index: I_InverseIndex[NumericTermInfoInDocument]

    def __init__(self, inv_ind: I_InverseIndex[NumericTermInfoInDocument]):
        self._inverse_index = inv_ind

    def amount_of_documents_containing_term(self, term: ITerm) -> int:
        return len(self._inverse_index[term])

    def get_numeric_info_of_term_in_document(self, term: ITerm,
                                             doc_id: DocumentIdentifier) -> NumericTermInfoInDocument:

        return self._inverse_index[term][doc_id]
