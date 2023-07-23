H, W, N = map(int, input().split())
blanks = set([tuple(map(int, input().split())) for _ in range(N)])
dp = [[0] * (W + 1) for _ in range(H + 1)]
ans = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if (i, j) not in blanks:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            ans += dp[i][j]
print(ans)
