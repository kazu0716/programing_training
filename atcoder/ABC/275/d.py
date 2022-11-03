from functools import lru_cache
from sys import setrecursionlimit

from pypyjit import set_param

set_param("max_unroll_recursion=-1")
setrecursionlimit(pow(10, 9))


@lru_cache(maxsize=None)
def func(k):
    if k == 0:
        return 1
    return func(k//2) + func(k//3)


N = int(input())
print(func(N))
