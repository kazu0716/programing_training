N = int(input())
dp = [i for i in range(N + 1)]
limit = 8
costs = sorted([pow(6, i) for i in range(limit) if pow(6, i) <= N] + [pow(9, i) for i in range(1, limit) if pow(9, i) <= N])
for i in range(N + 1):
    for c in costs:
        if i + c > N:
            break
        dp[i + c] = min(dp[i + c], dp[i] + 1)
print(dp[N])
