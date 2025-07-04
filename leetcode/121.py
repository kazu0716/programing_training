from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        min_price = pow(10, 9)
        max_profit = 0

        # NOTE: statement of if seems to be faster than min/max functions
        for price in prices:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
            if price < min_price:
                min_price = price
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    prices = [7, 6, 4, 3, 1]
    print(sol.maxProfit(prices))
