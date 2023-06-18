N, M = map(int, input().split())
INF = pow(10, 18)
xyz = [tuple(map(int, input().split())) for _ in range(N)]
ans = -INF
for bit in range(8):
    a = 1 if bool(bit >> 2 & 1) else -1
    b = 1 if bool(bit >> 1 & 1) else -1
    c = 1 if bool(bit & 1) else -1
    dp = [[-INF] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        x, y, z = xyz[i]
        add = a * x + b * y + c * z
        for j in range(N + 1):
            if dp[i][j] == -INF:
                continue
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + add)
    ans = max(ans, dp[-1][M])
print(ans)
