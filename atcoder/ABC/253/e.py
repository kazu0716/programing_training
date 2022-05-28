N, M, K = map(int, input().split())
MOD = 998244353
dp, sdp = [[0]*(M+1) for _ in range(N)], [[0]*(M+1) for _ in range(N)]
dp[0], sdp[0][1] = [0]+[1]*M, 1
for i in range(2, M+1):
    sdp[0][i] = sdp[0][i-1] + 1
for i in range(1, N):
    for j in range(1, M+1):
        if K == 0:
            dp[i][j] = sdp[i-1][-1] % MOD
        else:
            l, r = sdp[i-1][j-K] if j-K >= 1 else 0, sdp[i-1][-1] - sdp[i-1][j+K-1] if j+K <= M else 0
            dp[i][j] = (l+r) % MOD
        sdp[i][j] = (sdp[i][j-1] + dp[i][j]) % MOD
for i in range(2, M+1):
    dp[-1][i] = (dp[-1][i]+dp[-1][i-1]) % MOD
print(dp[-1][-1])
