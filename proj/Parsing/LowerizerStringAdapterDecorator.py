from StringAdapterWeakDecorator import *


class LowerizerStringAdapterWeakDecorator(StringAdapterWeakDecorator):
    def __init__(self, component: IStringAdapter) -> None:
        super().__init__(component)
        self._lowerized_value = str(self._component).lower()

    @property
    def _value(self) -> str:
        return self._lowerized_value
