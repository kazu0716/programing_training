from heapq import merge
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged: List[List[int]] = []
        intervals.sort()
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(sol.merge(intervals))
