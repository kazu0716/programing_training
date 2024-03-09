T = input()
N = int(input())
INF = pow(10, 18)
dp = [[INF] * (len(T) + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    AS = list(input().split())
    S = set(AS[1:])
    for j in range(len(T) + 1):
        if dp[i][j] >= INF:
            continue
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        for s in S:
            if T[j : j + len(s)] == s:
                dp[i + 1][j + len(s)] = min(dp[i + 1][j + len(s)], dp[i][j] + 1)
print(dp[-1][-1] if dp[-1][-1] < INF else -1)
