from abc import ABC

from StringAdapterDecorator import *

class LemmatizerStringAdapterDecorator(StringAdapterDecorator)
    def __init__(self, component: IStringAdapter) -> None:
        pass

    @property
    def _value(self) -> str:
        pass

    