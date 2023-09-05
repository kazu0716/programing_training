from collections import defaultdict

N = int(input())
INF = pow(10, 18)
dp = [defaultdict(lambda: INF) for _ in range(N + 1)]
dp[0][0] = 0
seats = 0
for i in range(N):
    X, Y, Z = map(int, input().split())
    seats += Z
    for j in dp[i]:
        if X > Y:
            dp[i + 1][j + Z] = min(dp[i + 1][j + Z], dp[i][j])
        else:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            dp[i + 1][j + Z] = min(dp[i + 1][j + Z], dp[i][j] + ((X + Y + 1) // 2) - X)
ans = INF
for i in range((seats + 1) // 2, seats + 1):
    ans = min(ans, dp[-1][i])
print(ans)
