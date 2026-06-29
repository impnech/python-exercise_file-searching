from AppConfig import get_class_implementation
from CorpusStructure.IDocument import IDocument

#tobedone config
class DocumentFactory:
    @classmethod
    def get_document_implementation(cls, *args, **kwargs) -> IDocument:
        return get_class_implementation(IDocument.__name__)(*args,**kwargs)


