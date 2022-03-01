from bisect import bisect_left
from sys import exit

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = tuple(map(int, input().split()))

for i in range(M):
    b = B[i]
    idx = bisect_left(A, b)
    if not A or idx >= len(A) or b != A[idx]:
        print("No")
        exit()
    A.remove(b)
print("Yes")
