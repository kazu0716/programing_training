from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = max_price = 0
        for price in prices[::-1]:
            max_profit = max(max_profit, max_price - price)
            max_price = max(max_price, price)
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))
