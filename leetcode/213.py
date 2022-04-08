from typing import List

from black import re


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        pre1 = cur1 = 0
        pre2 = cur2 = 0
        for i, num in enumerate(nums):
            if i < len(nums)-1:
                pre1, cur1 = cur1, max(pre1 + num, cur1)
            if i > 0:
                pre2, cur2 = cur2, max(pre2 + num, cur2)
        return max(cur1, cur2)


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 2]
    print(sol.rob(nums))
