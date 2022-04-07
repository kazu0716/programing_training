from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
            s = max(s, nums[i])
        return s


if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(nums))
