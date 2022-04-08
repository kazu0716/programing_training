from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0:2] = nums[0:2]
        ret = 0
        for i in range(len(nums)):
            for d in (2, 3):
                if i+d >= len(dp):
                    ret = max(ret, dp[i])
                else:
                    dp[i+d] = max(dp[i+d], dp[i] + nums[i+d])
        return ret


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.rob(nums))
