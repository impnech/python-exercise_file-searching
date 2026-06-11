from abc import ABC, abstractmethod


class ITerm(ABC):
    """
    Interface for terms (also often called "words") that form documents
    """

    @abstractmethod
    def __hash__(self) -> int:
        pass
