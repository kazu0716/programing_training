N, M, _ = map(int, input().split())
routes = []
for _ in range(M):
    A, B, C = map(int, input().split())
    routes.append((A-1, B-1, C))
E, INF = tuple(map(int, input().split())), pow(10, 18)
dp = [INF] * N
dp[0] = 0
for e in E:
    a, b, c = routes[e-1]
    if dp[a] < INF:
        dp[b] = min(dp[b], dp[a] + c)
print(dp[-1] if dp[-1] < INF else -1)
