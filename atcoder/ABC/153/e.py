H, N = map(int, input().split())
INF = pow(10, 18)

magic = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[INF]*(H+1) for _ in range(N+1)]

dp[0][H] = 0
for i in range(N):
    for h in range(H, -1, -1):
        if dp[i][h] == INF:
            continue
        dp[i+1][h] = min(dp[i+1][h], dp[i][h])
        hh = max(0, h - magic[i][0])
        dp[i][hh] = min(dp[i][hh], dp[i][h]+magic[i][1])

print(dp[-1][0])
