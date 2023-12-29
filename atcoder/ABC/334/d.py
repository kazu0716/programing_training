from bisect import bisect_left
from itertools import accumulate

N, Q = map(int, input().split())
R = sorted(list(map(int, input().split())))
s = [0] + list(accumulate(R))
ans = []
for _ in range(Q):
    X = int(input())
    i = bisect_left(s, X)
    ans.append(i if i < len(s) and s[i] == X else i - 1)
print(*ans, sep="\n")
