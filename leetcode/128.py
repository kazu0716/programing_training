from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(n)
        """
        num_set, finds, ans = set(nums), defaultdict(bool), 0
        for num in nums:
            if finds[num]:
                continue
            length, left, right = 1, num, num
            while left-1 in num_set:
                left -= 1
                length += 1
                finds[left] = True
            while right+1 in num_set:
                right += 1
                length += 1
                finds[right] = True
            ans = max(ans, length)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(sol.longestConsecutive(nums))
