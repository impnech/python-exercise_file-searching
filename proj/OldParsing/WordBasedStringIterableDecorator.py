from StringIterableWeakDecorator import *
from StringAdapterWeakDecorator import *


class WordBasedStringIterableWeakDecorator(StringIterableWeakDecorator):

    # TODO: associate a StringAdapterWeakDecorator, and use its __init__ or __new__
    def __init__(self, component: IStringIterableAdapter, word_WeakDecorator: StringAdapterWeakDecorator) -> None:
        super().__init__(component)
        self._word_WeakDecorator: StringAdapterWeakDecorator = word_WeakDecorator

        t= type(word_WeakDecorator)
        x = t.__new__(IStringAdapter("asdf"))
        raise NotImplemented("Word based list adapter")
        self._decorated_value: list[IStringAdapter] = [word_WeakDecorator(word) for word in component]


    @property
    def _value(self) -> Iterable[IStringAdapter]:
        pass
