from StringIterableWeakDecorator import *


class StopWordsRemoverStringIterableWeakDecorator(StringIterableWeakDecorator):
    def __init__(self, component: IStringIterableAdapter) -> None:
        super().__init__(component)

    @property
    def _value(self) -> Iterable[IStringAdapter]:
        return self.__value_without_stop_words