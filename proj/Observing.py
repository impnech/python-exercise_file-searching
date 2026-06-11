from typing import Any
from abc import ABC, abstractmethod


# from collections import Container, Iterable


class Observable(ABC):
    """
    SOLID-Warning: right now Observable uses list['Observer'] to contain its observers, it should be more generic
    """
    _observers: list['Observer']

    def __init__(self) -> None:
        self._observers: list['Observer'] = []

    def register_observer(self, observer: 'Observer') -> None:
        self._observers.append(observer)

    def unregister_observer(self, observer: 'Observer') -> None:
        self._observers.remove(observer)

    def notify_observers(self, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)


class Observer(ABC):

    def __init__(self, subject: Observable | None = None) -> None:
        if subject:
            subject.register_observer(self)

    @abstractmethod
    def notify(self, subject: Observable, *args: tuple[Any, ...], **kwargs: dict[str, Any]) -> None:
        """
        notify the observer (self) that something has changed in what it is observing.
        :param subject: the subject being observed and is being updated.
        :param args: all positional arguments that can be needed
        :param kwargs: all keyword arguments that can be needed
        """
        pass
