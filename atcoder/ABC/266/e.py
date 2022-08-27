from functools import lru_cache
from sys import setrecursionlimit

from pypyjit import set_param

set_param("max_unroll_recursion=-1")
setrecursionlimit(pow(10, 9))


@lru_cache(maxsize=None)
def get_expected_value(n: int) -> float:
    if n == 1:
        return s/6
    return sum([max(d, get_expected_value(n-1)) for d in dice])/6


N = int(input())
dice = (1, 2, 3, 4, 5, 6)
s = sum(dice)
print(get_expected_value(N))
