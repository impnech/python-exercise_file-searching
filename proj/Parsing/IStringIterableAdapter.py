
from IStringAdapter import *
from abc import *


class IStringIterableAdapter(Iterable[IStringAdapter], ABC):
    pass


