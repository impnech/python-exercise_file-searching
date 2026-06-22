from IStringAdapter import *


class AssociativeStringAdapter(IStringAdapter, ABC):
    """
    TODO: find some use for it or delete
    """
    @abstractmethod
    @property
    def _value(self) -> str:
        pass

    def __str__(self) -> str:
        return self._value


