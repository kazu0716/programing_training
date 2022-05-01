from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            if cnt[num] >= 2:
                del cnt[num]
        return tuple(cnt.keys())[0]


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1]
    print(sol.singleNumber(nums))
