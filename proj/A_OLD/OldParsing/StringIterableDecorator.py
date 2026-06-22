from AssociativeStringIterableAdapter import *
from IStringIterableAdapter import *
from abc import *


class StringIterableWeakDecorator(AssociativeStringIterableAdapter, ABC):

    @abstractmethod
    def __init__(self, component: IStringIterableAdapter) -> None:
        self._component: IStringIterableAdapter = component
