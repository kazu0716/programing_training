from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        queue, perm = deque([[num] for num in nums]), []
        while queue:
            cur = queue.popleft()
            for num in nums:
                if num in cur:
                    continue
                nxt = cur.copy()
                nxt.append(num)
                if len(nxt) == len(nums):
                    perm.append(nxt)
                    continue
                queue.append(nxt)
        return perm


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute(nums))
