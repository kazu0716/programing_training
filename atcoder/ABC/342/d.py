from collections import defaultdict
from typing import Dict

N = int(input())
A = list(map(int, input().split()))
# NOTE: prepare pow numbers for A
pows = [i**2 for i in range(max(A) + 1)]
cnt: Dict[int, int] = defaultdict(int)
ans = 0
for a in A:
    i = 2
    # NOTE: get min number by pows,
    # because when you multiply numbers that fall into that number together,
    # you get a square number.
    while i**2 <= a:
        while a % (i**2) == 0:
            a //= i**2
        i += 1
    # NOTE: add cnt which belongs to the same category to ans,
    # because we should count the number of pairs.
    ans += cnt[a]
    cnt[a] += 1
# NOTE: 0 makes all numbers square number in this statement.
print(ans + cnt[0] * (N - cnt[0]))
