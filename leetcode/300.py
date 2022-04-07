from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for i in range(1, len(nums)):
            if sub[-1] < nums[i]:
                sub.append(nums[i])
            else:
                sub[bisect_left(sub, nums[i])] = nums[i]
        return len(sub)


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(sol.lengthOfLIS(nums))
