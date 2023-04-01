from collections import defaultdict
from functools import reduce
from operator import mul


def comb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    return reduce(mul, range(n, n - r, -1)) // reduce(mul, range(1, r + 1))


S = input()
cur = [0] * 10
cnt = defaultdict(int)
cnt["0" * 10] += 1
for s in S:
    cur[int(s)] = int(not bool(cur[int(s)]))
    cnt["".join(list(map(str, cur)))] += 1
ans = 0
for v in cnt.values():
    if v >= 2:
        ans += comb(v, 2)
print(ans)
