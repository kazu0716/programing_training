from functools import reduce
from math import gcd

A, B, C = map(int, input().split())
g = reduce(gcd, (A, B, C))
print((A//g-1)+(B//g-1)+(C//g-1))
