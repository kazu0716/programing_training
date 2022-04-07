from collections import deque
from re import A
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0]*w for _ in range(h)]
        grid[0][0] = 1
        for i in range(h):
            for j in range(w):
                if (i == j == 0) or obstacleGrid[i][j] == 1:
                    continue
                grid[i][j] = (grid[i-1][j] if i > 0 else 0) + (grid[i][j-1] if j > 0 else 0)
        return grid[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    obstacleGrid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    print(sol.uniquePathsWithObstacles(obstacleGrid))
