from array import array
from bisect import bisect_left, insort_left

L, Q = map(int, input().split())

splits = array("I", [0, L])
ans = []

for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        insort_left(splits, x)
    else:
        idx = bisect_left(splits, x)
        ans.append(splits[idx] - splits[idx-1])

print(*ans, sep="\n")
