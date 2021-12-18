from bisect import bisect_right
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B, C = defaultdict(list), defaultdict(list)

for i in range(N):
    B[i+A[i]].append(i)
    C[i-A[i]].append(i)

ans = 0
for k in B:
    if k not in C:
        continue
    for v in B[k]:
        idx, l = bisect_right(C[k], v), len(C[k])
        if idx >= l:
            continue
        ans += l-idx

print(ans)
