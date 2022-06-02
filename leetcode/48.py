from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            # NOTE: transpose
            for j in range(i+1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # NOTE: reflect
            for k in range(len(matrix[i])//2):
                matrix[i][k], matrix[i][len(matrix[i])-k-1] = matrix[i][len(matrix[i])-k-1], matrix[i][k]
        print(matrix)


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix)
