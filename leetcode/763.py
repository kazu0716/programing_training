from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = defaultdict(list)
        for i, ss in enumerate(s):
            pos[ss].append(i)
        partition, cur = [], 0
        while cur < len(s):
            since, until = cur, pos[s[cur]][-1]
            while cur < len(s) and cur < until:
                until = max(until, pos[s[cur]][-1])
                cur += 1
            partition.append(until - since + 1)
            cur += 1
        return partition


if __name__ == "__main__":
    sol = Solution()
    # s = "ababcbacadefegdehijhklij"
    s = "eaaaabaaec"
    print(sol.partitionLabels(s))
