from abc import abstractmethod
from typing import Iterator
from numbers import Number

class CombineNumbers:
    @abstractmethod
    def combine(self, nums: Iterator[Number]) -> Number:
        raise NotImplementedError(f"Generic CombineNumbers doesn't have combine implementation")