from bisect import bisect_right
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Min heap solution

        Firstly, input first column nums to min_heap.
        Next, pop min num and push min num right number in width
        Finally, got the answer

        Time complexity: O((n^2)*log(n))
        Space complexity: O(n)
        """
        h, w, ans = len(matrix), len(matrix[0]), 0
        min_heap = [(matrix[i][0], i, 0) for i in range(min(k, h))]
        heapify(min_heap)
        for _ in range(k):
            ans, i, j = heappop(min_heap)
            if j < w-1:
                heappush(min_heap, (matrix[i][j+1], i, j+1))
        return ans

    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        """
        2 dimension binary search solution

        Firstly, consider binary search between min and max in matrix
        Next, count the number of above target by binary search in matrix
        Then, check the number over k or not
        Finally, got the answer

        Time complexity: O(n*log(n)*log(n))
        Space complexity: O(1)
        """
        low, high = matrix[0][0] - 1, matrix[-1][-1] + 1
        while high - low > 1:
            mid = (low + high) // 2
            if sum([bisect_right(row, mid) for row in matrix if row[0] <= mid]) < k:
                low = mid
            else:
                high = mid
        return high


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(sol.kthSmallest(matrix, k))
    print(sol.kthSmallest2(matrix, k))
