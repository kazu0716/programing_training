from collections import defaultdict

N, W = map(int, input().split())
dp = [defaultdict(int) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in tuple(dp[i-1].keys()):
        if dp[i][j] > 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j])
        else:
            dp[i][j] = dp[i-1][j]

        if dp[i-1][j] + w > W:
            continue

        if dp[i-1][j+v] > 0:
            dp[i][j+v] = min(dp[i-1][j] + w, dp[i-1][j+v])
        else:
            del dp[i-1][j+v]
            dp[i][j+v] = dp[i-1][j] + w

print(max(dp[-1].keys()))
