from IStringIterableAdapter import *


class AssociativeStringIterableAdapter(IStringIterableAdapter):
    @property
    @abstractmethod
    def _value(self) -> Iterable[IStringAdapter]:
        pass

    def __iter__(self):
        return self._value

