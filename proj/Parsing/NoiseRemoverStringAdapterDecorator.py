from StringAdapterDecorator import *
import re




class NoiseRemoverStringAdapterDecorator(StringAdapterDecorator):
    # TODO pull pattern from configuration
    pattern: str = r"[^\w\s]"

    def __init__(self, component: IStringAdapter):
        super().__init__(component)
        self._val_without_noise = re.sub(NoiseRemoverStringAdapterDecorator.pattern, "", str(self._component))
    @property
    def _value(self) -> str:
        return self._val_without_noise

