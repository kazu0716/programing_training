from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            hashmap[tuple(sorted(s))].append(s)
        return list(hashmap.values())


if __name__ == "__main__":
    sol = Solution()
    strs = list(list(input().replace("[", "").replace("]", "").replace("\"", "").split(",")))
    print(sol.groupAnagrams(strs))
