from Parsing.Lemmatizer import Lemmatizer
import nltk



class LemmatizerNLTK(Lemmatizer):
    @classmethod
    def _str_transform(cls, o_string):
        
        
        raise NotImplementedError("nltk lemma")



def main():
    l = LemmatizerNLTK
    text = "I am running in the park with my dogs".split()
    x= LemmatizerNLTK.transform(text)
    print(*x)

if __name__ == "__main__":
    main()