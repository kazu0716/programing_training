from collections import defaultdict

N, W = map(int, input().split())
INF = pow(10, 12)
dp = [defaultdict(lambda: INF) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in tuple(dp[i-1].keys()):
        dp[i][j] = min(dp[i-1][j], dp[i][j])
        if dp[i-1][j] + w > W:
            continue
        dp[i][j+v] = min(dp[i-1][j] + w, dp[i-1][j+v])

print(max(dp[-1].keys()))
