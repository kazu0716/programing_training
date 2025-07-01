# ref: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        def overwrite(n: int, idx: int, target: int) -> int:
            for _ in range(min(2, n)):
                nums[idx] = target
                idx += 1
            return idx

        wp, p1 = 0, 0
        for p2 in range(len(nums)):
            if nums[p1] != nums[p2]:
                wp = overwrite(p2 - p1, wp, nums[p1])
                p1 = p2
        wp = overwrite(p2 - p1 + 1, wp, nums[p2])
        del nums[wp:]
        print("nums:", nums)
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print(sol.removeDuplicates(nums))
