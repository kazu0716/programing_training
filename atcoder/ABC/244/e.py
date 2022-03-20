N, M, K, S, T, X = map(int, input().split())
edge = set()
MOD = 998244353
for _ in range(M):
    U, V = map(int, input().split())
    edge.add((U, V))
    edge.add((V, U))
dp = [[[0]*(N+1) for _ in range(K+1)] for _ in range(2)]
dp[S == X][0][S] = 1
for i in range(1, K+1):
    for u, v in edge:
        for k in range(2):
            dp[k ^ (v == X)][i][v] = (dp[k ^ (v == X)][i][v] + dp[k][i-1][u]) % MOD
print(dp[0][-1][T])
