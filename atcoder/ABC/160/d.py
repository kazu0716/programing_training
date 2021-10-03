N, X, Y = map(int, input().split())
INF = pow(10, 12)

dp = [[INF]*(N+1) for _ in range(N+1)]
dp[N][N] = 0
ans = [0]*(N)

for i in range(1, N):
    dp[i][i] = 0
    dp[i][i+1] = 1
    dp[i+1][i] = 1
    if i == X:
        dp[X][Y] = 1
        dp[Y][X] = 1

for i in range(1, N+1):
    for j in range(i, N):
        if i == j:
            continue
        dp[i][j+1] = min(dp[i][j+1], dp[i][j] + dp[j][j+1])
        dp[j+1][i] = min(dp[j+1][i], dp[j][i] + dp[j+1][j])

for i in range(1, N+1):
    for j in range(i, N+1):
        if i == j:
            continue
        dp[i][j] = min(dp[i][j], dp[i][X]+dp[X][Y]+dp[Y][j])
        dp[j][i] = min(dp[j][i], dp[X][i]+dp[Y][X]+dp[j][Y])

for i in range(1, N+1):
    for j in range(i, N+1):
        if i == j:
            continue
        dis = dp[i][j]
        ans[dis] += 1

print(*ans[1:], sep="\n")
