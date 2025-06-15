# ref: https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        wp = 0
        for rp in range(len(nums)):
            if nums[rp] != val:
                nums[wp] = nums[rp]
                wp += 1
        return wp


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(sol.removeElement(nums, val))
