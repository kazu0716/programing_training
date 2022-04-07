from collections import deque
from re import A
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0]*w for _ in range(h)]
        grid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(h):
            for j in range(w):
                if i + 1 < h and obstacleGrid[i+1][j] == 0:
                    grid[i+1][j] += grid[i][j]
                if j + 1 < w and obstacleGrid[i][j+1] == 0:
                    grid[i][j+1] += grid[i][j]
        return grid[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    obstacleGrid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    print(sol.uniquePathsWithObstacles(obstacleGrid))
