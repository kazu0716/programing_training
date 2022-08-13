N, L, R = map(int, input().split())
A = list(map(int, input().split()))
INF = pow(10, 18)
dp = [[INF]*3 for _ in range(N)]
dp[0] = [L, A[0], R]
for i in range(1, N):
    # NOTE: dp[i][0] -> before(i-1) using L, dp[i][1] -> before(i-1) using A[i-1], dp[i][2] -> before(i-1) using R
    dp[i][0] = dp[i-1][0] + L
    dp[i][1] = min(dp[i-1][0] + A[i], dp[i-1][1] + A[i])
    dp[i][2] = min(dp[i-1][1] + R, dp[i-1][2] + R)
print(min(dp[-1]))
