from bisect import bisect_right
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
cnt, sorted_uq_list = defaultdict(int), list(set(sorted(A)))
for a in A:
    idx = bisect_right(sorted_uq_list, a)
    if len(sorted_uq_list) <= idx:
        cnt[0] += 1
    else:
        cnt[len(sorted_uq_list)-idx] += 1
print(*[cnt[k] for k in range(N)], sep="\n")
