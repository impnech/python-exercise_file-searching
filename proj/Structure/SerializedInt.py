from pathlib import Path
import os


class SerializedInt:

    def __init__(self, path: Path | str, value_to_reset: int = None):
        self._path: Path | str = path
        if value_to_reset is not None:
            self.val = value_to_reset

    @property
    def val(self) -> int:
        try:
            with open(self._path, 'r') as storage_f:
                return int(storage_f.read().strip())
        except Exception:
            return 0

    @val.setter
    def val(self, new_val):
        with open(self._path, 'w') as storage_f:
            storage_f.write(str(new_val))

    def __getattr__(self, item):
        return self.val.__getattribute__(item)

    def __int__(self):
        return self.val.__int__()

    def __str__(self):
        return str(self.val)

    def __add__(self, other):
        return self.val.__add__(other)

    def __sub__(self, other):
        return self.val.__sub__(other)


if __name__ == '__main__':
    x = SerializedInt('new_file')
    print(x)
    print(x + 4)
    x += 3
    print(x)

    exit()


    class A:
        def __init__(self, val):
            self.val: str = val

        def __getattr__(self, item):
            return self.val.__getattribute__(item)


    x = A("23 aee")
    print(x.split())
    print(x.strip())
    print(x.__str__())
    x = A(6)
    print('\n\n\n')
    print(str(x), str(x.val), sep='\n')

    exit()
    x = SerializedInt(Path(r"new_file"))
    print(x.val)
    x.val = 23
    print(x.val)
    print(x.__str__())
    print(x.hi)
