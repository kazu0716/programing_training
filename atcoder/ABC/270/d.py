N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0]*(N+1)
for n in range(N+1):
    for k in range(K):
        if n - A[k] < 0:
            continue
        dp[n] = max(dp[n], A[k], n - dp[n - A[k]])
print(dp[-1])
