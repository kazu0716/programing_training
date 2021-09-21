N, W = map(int, input().split())
dp = [[0]*(W+1) for _ in range(N+1)]

w_range = range(W+1)

for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in w_range:
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j + w > W:
            continue
        dp[i][j+w] = max(dp[i][j+w], dp[i-1][j+w], dp[i-1][j] + v)

print(max(dp[-1]))
