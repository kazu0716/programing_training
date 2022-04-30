class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n):
            dp[i+1] += dp[i]
            if i+2 <= n:
                dp[i+2] += dp[i]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    n = 40
    print(sol.climbStairs(n))
