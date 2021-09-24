from math import ceil

N = int(input())
ZERO = 0.0
P = [ZERO] + list(map(float, input().split()))
dp = [[ZERO] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(N+1):
        p, q = P[i], 1-P[i]
        if i == 1 and j == 1:
            dp[i][j] = p
        elif i == 1 and j == 0:
            dp[i][j] = q
        else:
            dp[i][j-1] += dp[i-1][j-1] * q
            dp[i][j] += dp[i-1][j-1] * p

ans = ZERO
for j in range(ceil(N/2), N+1):
    ans += dp[-1][j]

print(ans)
