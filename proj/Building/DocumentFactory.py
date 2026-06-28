from AppConfig import get_class_implementation
from Building.IDocument import IDocument

#todo config
class DocumentFactory:
    @classmethod
    def get_document_implementation(cls, doc_id, *args, **kwargs) -> IDocument:
        return get_class_implementation(IDocument.__name__)(doc_id,*args,**kwargs)


