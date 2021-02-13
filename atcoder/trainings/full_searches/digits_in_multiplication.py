from math import sqrt

N = int(input())
ans = float("INF")

for A in range(1, int(sqrt(N))+1):
    B = N / A
    if N == A * B and B % 1 == 0:
        F = max(len(str(A)), len(str(int(B))))
        ans = min(ans, F)
print(int(ans))
