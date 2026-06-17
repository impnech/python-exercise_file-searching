import _io
import re
from typing import TextIO


gl_delim = r"\s"


def file_split(f: TextIO, delim: str = ',', bufsize: int = 1024):
    prev: str = ''
    while True:
        s: str = f.read(bufsize)
        if not s:
            break
        split: list[str] = re.split(delim, s)
        if len(split) > 1:
            yield prev + split[0]
            prev = split[-1]
            for x in split[1:-1]:
                yield x
        else:
            prev += s
    if prev:
        yield prev


if __name__ == '__main__':
    with open("../.gitignoreable/testing_python/files/ex-file.txt") as some_file:
        for chunk in file_split(some_file, gl_delim):
            print(f"{chunk=}")
