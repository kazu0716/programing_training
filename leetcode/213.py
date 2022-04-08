from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        def solve(nums: List[int]) -> int:
            pre = cur = 0
            for num in nums:
                pre, cur = cur, max(pre + num, cur)
            return cur

        if len(nums) == 1:
            return nums[0]
        return max(solve(nums[1:]), solve(nums[:-1]))


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 2]
    print(sol.rob(nums))
