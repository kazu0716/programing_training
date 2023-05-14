from functools import reduce
from math import gcd

N = int(input())
A = list(map(int, input().split()))
print(reduce(gcd, A))
