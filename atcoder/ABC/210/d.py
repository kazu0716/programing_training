H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

inf = pow(10, 18)
ans = inf

for _ in range(2):
    dp = [[inf] * (W+1) for _ in range(H+1)]
    for x in range(1, H+1):
        for y in range(1, W+1):
            dp[x][y] = min(A[x-1][y-1], dp[x-1][y]+C, dp[x][y-1]+C)

    for x in range(1, H+1):
        for y in range(1, W+1):
            cost = min(dp[x-1][y]+C+A[x-1][y-1], dp[x][y-1]+C+A[x-1][y-1])
            ans = min(ans, cost)

    for i in range(H):
        A[i] = A[i][::-1]

print(ans)
