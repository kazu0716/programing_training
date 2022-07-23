from collections import defaultdict

N, M = map(int, input().split())
X = list(map(int, input().split()))
bonus = defaultdict(int)
for _ in range(M):
    C, Y = map(int, input().split())
    bonus[C] = Y
dp = [[-1]*(N+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] > -1:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+X[i]+bonus[j+1])
            dp[i+1][0] = max(dp[i+1][0], dp[i][j])
print(max(dp[-1]))
