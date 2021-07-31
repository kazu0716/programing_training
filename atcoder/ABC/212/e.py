N, M, K = map(int, input().split())

graph = [[] for _ in range(N)]
dp = [[0] * N for _ in range(K+1)]
mod = 998244353

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

dp[0][0] = 1

for i in range(1, K+1):
    s = sum(dp[i-1])
    for j in range(N):
        cnt = 0
        for k in graph[j]:
            cnt = (cnt + dp[i-1][k]) % mod
        dp[i][j] = (s - dp[i-1][j] - cnt) % mod

print(dp[K][0])
