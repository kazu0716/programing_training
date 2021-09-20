N, K = map(int, input().split())
H = tuple(map(int, input().split()))

INF = pow(10, 9)
dp = [INF] * N
dp[0] = 0

for i in range(N-1):
    for k in range(1, K+1):
        if i+k < N:
            dp[i+k] = min(dp[i+k], dp[i]+abs(H[i+k]-H[i]))

print(dp[-1])
