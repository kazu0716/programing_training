from collections import defaultdict

D, G = map(int, input().split())
INF = pow(10, 18)
dp = [defaultdict(int) for _ in range(D + 1)]
dp[0][0] = 0
ans = INF
for i in range(D):
    p, c = map(int, input().split())
    for j in dp[i]:
        if dp[i][j] >= G:
            continue
        for k in range(p + 1):
            add = 100 * (i + 1) * k
            if k == p:
                add += c
            dp[i + 1][j + k] = max(dp[i + 1][j + k], dp[i][j] + add)
            if dp[i + 1][j + k] >= G:
                ans = min(ans, j + k)
print(ans)
