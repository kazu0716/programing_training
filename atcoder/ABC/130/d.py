from bisect import bisect_left
from itertools import accumulate

N, K = map(int, input().split())
A = tuple(map(int, input().split()))
S = tuple(accumulate(A))

ans = 0
for i in range(N):
    k = K if i == 0 else K + S[i-1]
    idx = bisect_left(S, k)
    if i-1 >= idx or idx >= N:
        continue
    ans += N - idx

print(ans)
