N = int(input())
MOD = 998244353

dp = [[0]*10 for _ in range(N)]
dp[0] = [1]*10
for i in range(1, N):
    for j in range(1, 10):
        if 1 <= j+1 <= 9:
            dp[i][j+1] = (dp[i][j+1]+dp[i-1][j]) % MOD
        if 1 <= j-1 <= 9:
            dp[i][j-1] = (dp[i][j-1]+dp[i-1][j]) % MOD
        dp[i][j] = (dp[i][j]+dp[i-1][j]) % MOD
ans = 0
for j in range(1, 10):
    ans = (ans+dp[-1][j]) % MOD
print(ans)
