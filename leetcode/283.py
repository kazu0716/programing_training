from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ini = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[ini] = nums[ini], nums[i]
                ini += 1


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 0, 3, 0, 15, 0, 12, 16, 0]
    sol.moveZeroes(nums)
