N, M, K = map(int, input().split())
MOD = 998244353

dp = [[0]*(K+1) for _ in range(N)]
for i in range(1, min(K+1, M+1)):
    dp[0][i] = 1
for i in range(N-1):
    for j in range(1, K+1):
        for k in range(1, min(K+1, M+1)):
            if j+k > K or dp[i][j] == 0:
                continue
            dp[i+1][j+k] = (dp[i+1][j+k] + dp[i][j]) % MOD
ans = 0
for i in range(1, K+1):
    ans = (ans + dp[-1][i]) % MOD
print(ans)
