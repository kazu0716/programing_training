from functools import lru_cache
from sys import setrecursionlimit

import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')
setrecursionlimit(pow(10, 6))


@lru_cache(maxsize=1000)
def solve(n):
    if n == 1:
        return [1]
    return solve(n-1) + [n] + solve(n-1)


N = int(input())
print(*solve(N))
