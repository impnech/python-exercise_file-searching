import unittest
from Parsing.StopwordsRemover import StopwordsRemover
from Parsing.NoiseRemover import *
from not_used_yet.IDsAndStreamsGenerator import *

class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_something():
        f_path = "../files/sample_texts/file1.txt"
        with open(f_path) as f:
            res = file_split(f)
            print(list(res))

            f.seek(0)
            li = list(StopwordsRemover.transform(NoiseRemover.transform(Lowerizer.transform(file_split(f)))))
            print(li)
            print(*li, sep='#')

    @staticmethod
    def pairs():
        pass


if __name__ == '__main__':
    unittest.main()
