# ref: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        wp = 0
        for rp in range(1, len(nums)):
            if nums[wp] != nums[rp]:
                wp += 1
                nums[wp] = nums[rp]
        return wp + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(sol.removeDuplicates(nums))
