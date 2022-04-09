from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices[:-1]):
            profit = prices[i+1] - price
            if profit > 0:
                max_profit += profit
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))
