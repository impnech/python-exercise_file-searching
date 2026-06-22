from abc import *
from typing import *

KT = TypeVar('KT', bound=Hashable)
VT = TypeVar('VT')


class MapHandler(ABC, Generic[KT, VT], Mapping[KT, VT]):
    pass

