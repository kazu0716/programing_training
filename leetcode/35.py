from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = -1, len(nums)
        while high - low > 1:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid
        return high


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 0
    print(sol.searchInsert(nums, target))
