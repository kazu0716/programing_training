from functools import reduce
from math import gcd

N = int(input())
A = list(map(int, input().split()))
target = reduce(gcd, A)
ans = 0
for a in A:
    p = a // target
    while p % 2 == 0:
        p //= 2
        ans += 1
    while p % 3 == 0:
        p //= 3
        ans += 1
    if p != 1:
        print(-1)
        exit()
print(ans)
