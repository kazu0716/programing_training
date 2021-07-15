import math
from functools import reduce


def gcd(*n):
    return reduce(math.gcd, n)


def lcm(n):
    g = gcd(*n)
    s = 1
    for i in range(N):
        s *= A[i]//g
    return s * g


N = int(input())
A = list(map(int, input().split()))
cnt, l = 0, lcm(A)

for i in range(N):
    cnt += l//A[i]

print(l/cnt)
