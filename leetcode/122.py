from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        INF = pow(10, 9)
        min_price, sum_profits = INF, 0
        for price in prices:
            profit = price - min_price
            if profit > 0:
                sum_profits += profit
                min_price = INF
            if min_price > price:
                min_price = price
        return sum_profits


if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))
