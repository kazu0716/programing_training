N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())
MOD = 998244353
blocks = set([tuple(map(int, input().split())) for _ in range(M)])
dp = [[[0]*(N+2) for _ in range(N+2)] for _ in range(N+2)]
ans, dp[0][0][0] = 0, 1
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            x, y = A*i + C*j + E*k, B*i + D*j + F*k
            if (x, y) in blocks:
                dp[i][j][k] = 0
                continue
            if i+j+k == N:
                ans = (ans + dp[i][j][k]) % MOD
            elif i+j+k+1 > N:
                break
            dp[i+1][j][k] = (dp[i+1][j][k] + dp[i][j][k]) % MOD
            dp[i][j+1][k] = (dp[i][j+1][k] + dp[i][j][k]) % MOD
            dp[i][j][k+1] = (dp[i][j][k+1] + dp[i][j][k]) % MOD
print(ans)
