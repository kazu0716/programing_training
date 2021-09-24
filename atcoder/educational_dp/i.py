N = int(input())
P = [0.0] + list(map(float, input().split()))
dp = [[0.0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(N+1):
        dp[i][j-1] += dp[i-1][j-1] * (1.0 - P[i])
        dp[i][j] += dp[i-1][j-1] * P[i]

print(sum([dp[-1][j] for j in range(N//2+1, N+1)]))
