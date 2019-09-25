"""Pi approximation"""
from decimal import getcontext, Decimal as D
import functools
import sys

sys.setrecursionlimit(100000)


@functools.lru_cache(maxsize=3)
def side_length(n: int) -> D:
    """Calculates the length of a polygon-side for a given depth recursively

    :param n: recursion-depth
    :type n: int
    :returns: length of a polygon-side with (2 ** n) * 3 corners
    :rtype: Decimal
    """
    if n <= 1:
        return D(1)

    return D(
        D(2) - D(D(4) - side_length(n - 1) ** 2).sqrt()
    ).sqrt()


def approx_pi(iterations: int, precision: int) -> D:
    """Approximates pi

    :param iterations: iteration-steps to perform; polygon with
    (2 ** iterations) * 3 corners to use for the approximation
    :type iterations: int
    :param precision: precision to use (default is iterations * 4)
    :type precision: int
    :returns: approximation for pi
    :rtype: Decimal
    """
    getcontext().prec = precision if precision else iterations * 4

    return side_length(iterations) * (D(2) ** D(iterations)) * D(1.5)
