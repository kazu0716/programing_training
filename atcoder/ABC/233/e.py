from collections import defaultdict
from itertools import accumulate

X = tuple(map(int, tuple(input())))
S = tuple(accumulate(X))[::-1]
ans = defaultdict(int)

for i in range(len(X)):
    cur = S[i]
    while cur > 0:
        q, r = divmod(ans[i] + cur % 10, 10)
        ans[i] = r
        cur = cur//10 + q
        i += 1

print(*[ans[k] for k in range(len(ans)-1, -1, -1)], sep="")
