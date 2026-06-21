import re
from WordBasedStringStreamTransformer import *



class NoiseRemover(WordBasedStreamStringTransformer):
    # TODO pull pattern from configuration
    pattern: str = r"[^\w\s-]"

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



