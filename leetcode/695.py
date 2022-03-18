from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        finds = [[False]*len(grid[0]) for _ in range(len(grid))]
        mx_lands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if finds[i][j] or grid[i][j] == 0:
                    continue
                finds[i][j] = True
                stack = [(i, j)]
                lands = 0
                while stack:
                    cur_i, cur_j = stack.pop()
                    lands += 1
                    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        nxt_i, nxt_j = cur_i+di, cur_j+dj
                        if 0 > nxt_i or nxt_i >= len(grid) or 0 > nxt_j or nxt_j >= len(grid[0]) or finds[nxt_i][nxt_j] or grid[nxt_i][nxt_j] == 0:
                            continue
                        finds[nxt_i][nxt_j] = True
                        stack.append((nxt_i, nxt_j))
                mx_lands = max(mx_lands, lands)
        return mx_lands


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(sol.maxAreaOfIsland(grid))
