import re
from Parsing.WordBasedStringStreamTransformer import *
from AppConfig import get_default_value


class NoiseRemover(WordBasedStreamStringTransformer):
    
    pattern:str = get_default_value("noise_to_remove")

    @classmethod
    def _str_transform(cls, o_string: str) -> str:
        return re.sub(pattern=NoiseRemover.pattern, string=o_string, repl="")


if __name__ == '__main__':
    text = "lkajsdflkj afd-sdf,sdfkj .wfk=sd__f-asf+asdfjkl_fjklj\fsdf}sdf][asdf/sdf \0, \nasdf\tafda%@#%$fasaf"
    print(*NoiseRemover.transform(text.split()))
    def it():
        for w in text.split():
            yield w
    print(*NoiseRemover.transform((it())))



