from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        finds = [[False]*len(grid[0]) for _ in range(len(grid))]
        lands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if finds[i][j] or grid[i][j] == "0":
                    continue
                finds[i][j] = True
                stack = [(i, j)]
                while stack:
                    cur_i, cur_j = stack.pop()
                    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        nxt_i, nxt_j = cur_i+di, cur_j+dj
                        if 0 > nxt_i or nxt_i >= len(grid) or 0 > nxt_j or nxt_j >= len(grid[0]) or finds[nxt_i][nxt_j] or grid[nxt_i][nxt_j] == "0":
                            continue
                        finds[nxt_i][nxt_j] = True
                        stack.append((nxt_i, nxt_j))
                lands += 1
        return lands


if __name__ == "__main__":
    sol = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(sol.numIslands(grid))
