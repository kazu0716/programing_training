from collections import deque
from copy import deepcopy

N, K = map(int, input().split())

F = [[0]*N for _ in range(N)]
dp = [[[] for _ in range((N-K+1))] for _ in range((N-K+1))]
for i in range(N):
    A = list(map(int, input().split()))
    for j, a in enumerate(A):
        F[i][j] = a

tmp = []
for i in range(K):
    for j in range(K):
        tmp.append(F[i][j])
print(tmp)
dp[0][0] = deque(tmp)


for i in range(N-K):
    for j in range(N-K):
        tmp1 = deepcopy(dp[i][j])

        tmp2 = deepcopy(dp[i][j])
        for k in range(K):
            tmp2.popleft()
            tmp2.append(F[i+K][j+k])
        dp[i+1][j] = tmp2
print(dp)
