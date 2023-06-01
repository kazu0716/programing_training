from functools import reduce
from math import gcd

N, X = map(int, input().split())
x = list(map(int, input().split()))
print(reduce(gcd, [abs(xx - X) for xx in x]))
