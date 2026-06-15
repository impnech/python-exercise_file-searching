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


