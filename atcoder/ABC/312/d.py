S = input()
MOD = 998244353
dp = [[0] * (len(S) + 1) for _ in range(len(S) + 1)]
dp[0][0] = 1
for i, s in enumerate(S):
    for j in range(len(S) + 1):
        if (s == "(" or s == "?") and j < len(S):
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
        if (s == ")" or s == "?") and j > 0:
            dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD
print(dp[-1][0])
