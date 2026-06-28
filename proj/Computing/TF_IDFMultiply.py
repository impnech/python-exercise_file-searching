from Computing.TF_IDF import TF_IDF
from pathlib import Path

class TF_IDFMultiply(TF_IDF):
    """
    calculates tf_idf by multiplying the tf and idf values
    """
    def calc_from_numbers(self, tf, idf):
        return tf*idf
    

if __name__ == "__main__":

    from Building.StringTerm import StringTerm
    _path = Path(__file__).parent.parent/"files/sample_texts/file1.txt"
    print(_path)
    w1 = "deep"
    w2 = StringTerm("space")
    print(f"{w1=}, {str(w2)=},")

    
    c = TF_IDFMultiply()
    v1 = c.unsafe_calc(w1,_path)
    print(f'{v1=}')
    v1_1 = c.calc(w1,_path)
    print(f'{v1_1=}')
    v2 = c.calc(w2,_path)
    print(f'{v2=}')

    print(f" {v1=}, {v1_1=},{v2=}")