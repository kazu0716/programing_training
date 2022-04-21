from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(pow(10, 9))


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        @lru_cache(maxsize=None)
        def solve(n, k):
            if n == 1:
                return 0
            mid = 2**(n-2)
            if k > mid:
                return int(not solve(n-1, k-mid))
            else:
                return solve(n-1, k)
        return solve(n, k)


if __name__ == "__main__":
    sol = Solution()
    n = 20
    k = pow(2, n-1)
    print(sol.kthGrammar(n, k))
