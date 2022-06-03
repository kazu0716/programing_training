from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        INF, H, W = pow(10, 18), len(grid), len(grid[0])
        dp = [[INF]*W for _ in range(H)]
        dp[0][0] = grid[0][0]
        for i in range(H):
            for j in range(W):
                if i-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
                if j-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(sol.minPathSum(grid))
