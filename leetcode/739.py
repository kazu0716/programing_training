from heapq import heappop, heappush
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, heap = [0]*len(temperatures), []
        for i, t in enumerate(temperatures):
            while heap and t > heap[0][0]:
                _, j = heappop(heap)
                ans[j] = i-j
            heappush(heap, (t, i))
        return ans


if __name__ == "__main__":
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(temperatures))
