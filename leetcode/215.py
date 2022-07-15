from random import choice
from sys import setrecursionlimit
from typing import List

setrecursionlimit(pow(10, 9))


class Solution:
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """
        Time complexity : O(NlogN)
        Space complexity : O(N)
        """
        return sorted(nums, reverse=True)[k-1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time complexity : O(N)
        Space complexity : O(N)
        """
        pivot = choice(nums)
        low, high = [n for n in nums if n < pivot], [n for n in nums if n > pivot]
        p_cnt = nums.count(pivot)
        if k <= len(high):
            return self.findKthLargest(high, k)
        elif k > len(high) + p_cnt:
            return self.findKthLargest(low, k-len(high)-p_cnt)
        else:
            return pivot


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(sol.findKthLargest2(nums, k))
