from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s_hash, cnt = defaultdict(list), 0
        _sum, s_hash[0] = [0], [0]
        for i, num in enumerate(nums):
            cnt += num
            _sum.append(cnt)
            s_hash[cnt].append(i+1)
        ret = 0
        for i, s in enumerate(_sum):
            tar = s + k
            if tar not in s_hash:
                continue
            idx = bisect_right(s_hash[tar], i)
            if len(s_hash[tar]) <= idx:
                continue
            ret += len(s_hash[tar]) - idx
        return ret


if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int, list(input().replace("[", "").replace("]", "").replace("\"", "").split(","))))
    k = int(input())
    print(sol.subarraySum(nums, k))
