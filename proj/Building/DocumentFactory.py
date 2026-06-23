from Building.DocumentByPath import *


class DocumentFactory:
    @classmethod
    def get_document(cls, doc_id, *args, **kwargs):
        return DocumentByPath(doc_id)


