N = int(input())
INF = pow(10, 9)
X, Y = map(int, input().split())

dp = [[[INF] * (Y+1) for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(1, N+1):
    A, B = map(int, input().split())
    for j in range(X+1):
        for k in range(Y+1):
            x, y = min(j+A, X), min(k+B, Y)
            dp[i][x][y] = min(dp[i][x][y], dp[i-1][j][k]+1)
            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])

ans = dp[-1][X][Y]

if ans == INF:
    print(-1)
else:
    print(ans)
