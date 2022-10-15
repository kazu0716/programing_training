from math import gcd

N = int(input())
A = list(map(int, input().split()))
g = 0
for i in range(N-1):
    g = gcd(g, abs(A[i] - A[i+1]))
print(2 if g == 1 else 1)
