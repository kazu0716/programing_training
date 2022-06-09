class Solution:
    def numTrees(self, n: int) -> int:
        """
        DP solution

        Time complexity: O(n^2)
        Auxiliary Space: O(n)
        """
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.numTrees(n))
