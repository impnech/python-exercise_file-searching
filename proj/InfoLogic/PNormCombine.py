from InfoLogic.CombineNumbers import CombineNumbers, Iterator, Number


class PNormCombine(CombineNumbers):
    """
    calculates p-norm of a list of numbers.
    worth noting that when p=1 (default in here), it's just the sum of absolute values
    (in mathematical terminology, p-norm)
    """

    def __init__(self, p: Number = None):
        if p is None: p = 1
        if not isinstance(p, Number) or p < 0:
            raise ValueError(f"p-norm is not defined for p<0, got {p=}")
        self._p = p

    def combine(self, nums: Iterator[Number]) -> Number:
        p = self._p
        if p is None or p == 1:
            return sum(abs(num) for num in nums)  # unnecessary, but more efficient than the general case
        return sum(abs(num) ** p for num in nums) ** (1 / p)
