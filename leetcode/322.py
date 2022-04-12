from functools import lru_cache
from sys import setrecursionlimit
from typing import List

setrecursionlimit(pow(10, 9))


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = pow(10, 18)

        @lru_cache(None)
        def dfs(amount):
            if amount == 0:
                return 0
            n = INF
            for coin in coins:
                if amount >= coin:
                    n = min(n, dfs(amount - coin) + 1)
            return n

        num = dfs(amount)
        return num if num != INF else -1


if __name__ == "__main__":
    sol = Solution()
    coins = [186, 419, 83, 408]
    amount = 6249
    print(sol.coinChange(coins, amount))
