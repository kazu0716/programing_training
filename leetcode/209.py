from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r, cnt = 0, 0
        min_length = pow(10, 9)
        for l in range(len(nums)):
            while r < len(nums) and cnt < target:
                cnt += nums[r]
                r += 1
            if cnt >= target:
                min_length = min(min_length, r-l)
            cnt -= nums[l]
        return 0 if min_length == pow(10, 9) else min_length


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print(sol.minSubArrayLen(target, nums))
