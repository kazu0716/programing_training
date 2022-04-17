from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        low, high = 0, len(nums)-1
        while high - low > 1:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid
            else:
                high = mid
        return nums[high]


if __name__ == "__main__":
    sol = Solution()
    nums = [13, 15, 17, 11]
    print(sol.findMin(nums))
