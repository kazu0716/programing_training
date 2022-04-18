from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        if nums[0] != 0:
            dp[0][nums[0]], dp[0][-nums[0]] = 1, 1
        else:
            dp[0][nums[0]], dp[0][-nums[0]] = 2, 2
        for i in range(1, len(nums)):
            for j in dp[i-1]:
                dp[i][j+nums[i]] += dp[i-1][j]
                dp[i][j-nums[i]] += dp[i-1][j]
        return dp[-1][target]


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    target = 1
    print(sol.findTargetSumWays(nums, target))
