from IStringAdapter import *
from AssociativeStringAdapter import *


class StringAdapterDecorator(AssociativeStringAdapter):

    @abstractmethod
    def __init__(self, component: IStringAdapter) -> None:
        """
        Needs to still set self._val, based on the decorator
        :param component:
        """
        self._component: IStringAdapter = component
        self._val: str


