from collections import defaultdict

N, K, P = map(int, input().split())
C, A = [], []
INF = pow(10, 18)
for _ in range(N):
    CA = list(map(int, input().split()))
    C.append(CA[0])
    A.append(CA[1:])
dp = [defaultdict(lambda: INF) for _ in range(N + 1)]
dp[0][tuple([0] * K)] = 0
for i in range(N):
    for params in dp[i]:
        dp[i + 1][params] = min(dp[i + 1][params], dp[i][params])
        nxt_params = list(params)
        for j in range(K):
            nxt_params[j] = min(nxt_params[j] + A[i][j], P)
        nxt_params = tuple(nxt_params)
        dp[i + 1][nxt_params] = min(dp[i + 1][nxt_params], dp[i][params] + C[i])
ans = dp[-1][tuple([P] * K)]
print(ans if ans < INF else -1)
