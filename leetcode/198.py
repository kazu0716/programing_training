from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        pre = cur = 0
        for num in nums:
            pre, cur = cur, max(pre + num, cur)
        return cur


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.rob(nums))
