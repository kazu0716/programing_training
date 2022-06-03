from collections import defaultdict
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        H, W = len(matrix), len(matrix[0])
        horizontal, vertical = defaultdict(bool), defaultdict(bool)
        for i in range(H):
            for j in range(W):
                if matrix[i][j] == 0:
                    horizontal[i], vertical[j] = True, True
        for h in horizontal:
            for w in range(W):
                matrix[h][w] = 0
        for v in vertical:
            for h in range(H):
                matrix[h][v] = 0
        print(matrix)


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix)
