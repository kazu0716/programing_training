from copy import deepcopy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        origin = deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[j][len(matrix[i])-i-1] = origin[i][j]


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix)
