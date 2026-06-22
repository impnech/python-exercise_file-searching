import _io
import re
from typing import TextIO
from typing import *

# TODO put this in config
gl_delim = r"\s"




def file_split(f: TextIO, delim: str = gl_delim, bufsize: int = 1024) -> Iterator[str]:
    if delim is None: delim = gl_delim
    prev: str = ''
    while True:
        # because of the way split and re.split work, the edge case when f.read() read a ws last, is fine.
        # but, the default str::split is different than str::split(' \t\n...')
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


def stream_reorganize(o_stream: Iterator[str] | Iterable[str], delim: str = gl_delim) -> Iterator[str]:
    raise NotImplemented(f"{stream_reorganize.__name__}")

    if delim is None: delim = gl_delim
    prev: str = ''
    for s in o_stream:
        split: list[str] = re.split(delim, s)
        if len(split) > 1:
            yield prev + split[0]
            prev = split[-1]
            # all but the first which is together with prev.
            for x in split[1:-1]:
                yield x
        else:
            prev += s
    if prev:
        yield prev


if __name__ == '__main__':
    path = r"tmpnew"

    text = " ahi ojlk "
    with open(path, "w"):
        pass
    with open(path, "r+") as f:
        f.write(text)
        f.seek(0)
        print(list(file_split(f, bufsize=5)))

    print(re.split(pattern=r'\s', string=text))
    print(text.split(r' '))


    exit()
    with open("../.gitignoreable/testing_python/files/ex-file.txt") as some_file:
        for chunk in file_split(some_file, gl_delim):
            print(f"{chunk=}")
