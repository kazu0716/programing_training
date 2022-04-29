from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(left: int, right: int) -> None:
            nonlocal nums
            for i in range((left+right)//2+1-left):
                nums[left+i], nums[right-i] = nums[right-i], nums[left+i]

        l = len(nums)-2
        while l >= 0 and nums[l] >= nums[l+1]:
            l -= 1
        if l == -1:
            swap(0, len(nums)-1)
            return
        r = len(nums)-1
        while nums[r] <= nums[l]:
            r -= 1
        nums[l], nums[r] = nums[r], nums[l]
        swap(l+1, len(nums)-1)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 2]
    sol.nextPermutation(nums)
