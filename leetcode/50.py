from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(pow(10, 9))


class Solution:
    @lru_cache(maxsize=None)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x*x, n//2)
        return x * self.myPow(x, n-1)


if __name__ == "__main__":
    sol = Solution()
    x = 0.00001
    n = 2147483647
    print(sol.myPow(x, n))
