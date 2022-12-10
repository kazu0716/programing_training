N, K, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[-1] * (K + 1) for _ in range(D)] for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(D):
        for k in range(K + 1):
            if dp[i][j][k] == -1:
                continue
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
            if k < K:
                dp[i+1][(j + A[i-1]) % D][k+1] = max(dp[i+1][(j + A[i-1]) % D][k+1], dp[i][j][k] + A[i-1])
print(dp[-1][0][-1])
