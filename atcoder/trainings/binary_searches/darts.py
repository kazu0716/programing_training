import itertools
from bisect import bisect_left

N, M = map(int, input().split())
P = [int(input()) for _ in range(N)]

P.append(0)
S, ans = [], 0

for i in range(N):
    for j in range(i, N+1):
        S.append(P[i]+P[j])

S.append(0)
S.sort()

for i in range(len(S)):
    if M - S[i] > 0:
        idx = bisect_left(S, M - S[i])
        if idx > 0 and S[idx-1]+S[i] <= M:
            ans = max(S[idx-1]+S[i], ans)

print(ans)
