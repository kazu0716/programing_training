N, _ = map(int, input().split())
A = sorted(list(map(int, input().split())))
MATCH = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
dp = [-1] * (N + 1)
dp[0] = 0
for i in range(N + 1):
    for a in A:
        if dp[i] < 0 or i + MATCH[a] > N:
            continue
        dp[i + MATCH[a]] = max(dp[i + MATCH[a]], 10 * dp[i] + a)
print(dp[-1])
