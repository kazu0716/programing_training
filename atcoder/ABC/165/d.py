from math import floor

A, B, N = map(int, input().split())
x = B - 1 if N >= B - 1 else N
ans = floor(A*x/B) - A*floor(x/B)
print(ans)
