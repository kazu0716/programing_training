N, M = map(int, input().split())
A = list(map(int, input().split()))
INF = pow(10, 18)
dp = [[-INF]*(M+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(min(i+1, M+1)):
        dp[i][j] = 0 if j == 0 else max(dp[i-1][j], dp[i-1][j-1] + j*A[i-1])
print(dp[-1][-1])
