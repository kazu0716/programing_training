H, W = map(int, input().split())

dp = [[0]*W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j, s in enumerate(list(input())):
        if s == "#":
            dp[i][j] = -1

ans = 0
for i in range(H):
    for j in range(W):
        if j + 1 < W and dp[i][j] > 0 and dp[i][j+1] > -1:
            dp[i][j+1] = max(dp[i][j] + 1, dp[i][j+1])
        if i + 1 < H and dp[i][j] > 0 and dp[i+1][j] > -1:
            dp[i+1][j] = max(dp[i][j] + 1, dp[i+1][j])
        ans = max(ans, dp[i][j])

print(ans)
