from typing import *
from abc import *


class IStringAdapter(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    def __eq__(self, other):
        if not isinstance(other, str | IStringAdapter):
            return False
        return str(other) == str(self)
    def __hash__(self) -> int:
        return hash(str(self))

    def __add__(self, other: 'IStringAdapter' | str):
        # TODO: log it properly if it's so important to note
        print(f"{IStringAdapter.__name__} is adding {self} with {other}.")
        return str(self) + str(other)


