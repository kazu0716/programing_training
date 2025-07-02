# ref: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Original List                   : 1 2 3 4 5 6 7
        After reversing all numbers     : 7 6 5 4 3 2 1
        After reversing first k numbers : 5 6 7 4 3 2 1
        After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

        Time Complexity: O(N)
        Space Complexity: O(1)
        """

        def reverse(head: int, tail: int) -> None:
            while head < tail:
                nums[head], nums[tail] = nums[tail], nums[head]
                head += 1
                tail -= 1

        n = len(nums)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        print("nums:", nums)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(sol.rotate(nums, k))
