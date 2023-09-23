from bisect import bisect_right
from itertools import accumulate

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))
B_sum = [0] + list(accumulate(B))
ans = 0
for i in range(N):
    idx = bisect_right(B, P - A[i])
    ans += A[i] * idx + B_sum[idx] + P * (M - idx)
print(ans)
