from collections import deque
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]
        sub, queue = [[]] + [[num] for num in nums], deque([[num] for num in nums])
        while queue:
            cur = queue.popleft()
            for num in nums:
                if num in cur:
                    continue
                nxt = cur.copy()
                nxt.append(num)
                if sorted(nxt) not in sub and len(nxt) <= len(nums):
                    sub.append(sorted(nxt))
                    if len(nxt) < len(nums):
                        queue.append(nxt)
        return sub


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 10, 0]
    print(sol.subsets(nums))
