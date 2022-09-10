from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(pow(10, 9))


class Solution:
    @lru_cache(maxsize=None)
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(n//2) + 1
        else:
            return min(self.integerReplacement(n+1) + 1, self.integerReplacement(n-1) + 1)


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.integerReplacement(n))
