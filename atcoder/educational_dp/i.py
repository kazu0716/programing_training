N = int(input())
P = [0.0] + list(map(float, input().split()))
dp = [[0.0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(N+1):
        p, q = P[i], 1.0 - P[i]
        if i == 1 and j == 1:
            dp[i][j] = p
        elif i == 1 and j == 0:
            dp[i][j] = q
        else:
            dp[i][j-1] += dp[i-1][j-1] * q
            dp[i][j] += dp[i-1][j-1] * p

print(sum([dp[-1][j] for j in range(N//2+1, N+1)]))
