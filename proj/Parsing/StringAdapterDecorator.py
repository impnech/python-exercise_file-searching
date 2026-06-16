from IStringAdapter import *
from AssociativeStringAdapter import *


class StringAdapterWeakDecorator(AssociativeStringAdapter):

    @abstractmethod
    def __init__(self, component: IStringAdapter) -> None:
        """
        self._component: IStringAdapter = component
        """

        pass

