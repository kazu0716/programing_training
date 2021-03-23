from itertools import product
from math import ceil, floor

A, B, W = map(float, input().split())

w = W * 1000
upper = int(floor(w/A))
lower = int(ceil(w/B))

if upper < lower:
    print("UNSATISFIABLE")
else:
    print(lower, upper)
