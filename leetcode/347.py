from collections import Counter, defaultdict
from heapq import heappop, heappush
from typing import Dict, List, Tuple


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        ans: List[Tuple[int, int]] = []
        print(cnt)
        for key in cnt:
            if len(ans) == k:
                v, _k = heappop(ans)
                if cnt[key] > v:
                    heappush(ans, (cnt[key], key))
                else:
                    heappush(ans, (v, _k))
            else:
                heappush(ans, (cnt[key], key))
        return [k for _, k in ans]


if __name__ == "__main__":
    input_list = list(map(int, list(input().replace("[", "").replace("]", "").split(","))))
    k = int(input())
    sol = Solution()
    print(sol.topKFrequent(input_list, k))
