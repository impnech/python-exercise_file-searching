from CorpusStructure.IDocument import DocumentIdentifier
from CorpusStructure.ITerm import ITerm
from AppConfig import get_class_implementation
from InfoLogic.TF import TF
from InfoLogic.InvertedIndexCounter import InvertedIndexCounter
from CorpusStructure.DocumentsHolder import DocumentsHolder

class TFdivBySum(TF):
    """
    Calculates the term frequency by dividing the term frequency in a document (f_td) by the document size |d| .
    """
    
    def calc(self, term: ITerm, doc_id: DocumentIdentifier) -> float:
        counter: InvertedIndexCounter = get_class_implementation(InvertedIndexCounter.__name__)() 
        ftd: int = counter[term].get(doc_id,0)
        d_size: int = DocumentsHolder()[doc_id].length

        return ftd/d_size


if __name__ == '__main__':
    pass
    tf = TFdivBySum()
    for k in tf:
        pass#print(k)

    for item in tf.items():
        pass#print(*item)
    
    from pathlib import Path
    _pa =Path(__file__).parent.parent / "files/sample_files/file1"

    print(tf["deep"])
    print(tf["deep"].get(_pa,0))



