N, X, Y = map(int, input().split())

dp = [[0]*(N+1) for _ in range(N+1)]
ans = [0]*(N)

for k in range(3):
    for i in range(1, N+1):
        for j in range(i, N+1):
            if i == j:
                continue
            if k == 0:
                if i == X and j == Y:
                    dp[X][Y], dp[Y][X] = 1, 1
                else:
                    dp[i][j], dp[j][i] = abs(i-j), abs(i-j)
            if k == 1:
                dp[i][j] = min(dp[i][j], dp[i][X]+dp[X][Y]+dp[Y][j])
                dp[j][i] = min(dp[j][i], dp[X][i]+dp[Y][X]+dp[j][Y])
            elif k == 2:
                dis = dp[i][j]
                ans[dis] += 1

print(*ans[1:], sep="\n")
