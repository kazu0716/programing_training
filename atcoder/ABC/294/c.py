from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A + B)
for i in range(N):
    A[i] = bisect_left(C, A[i]) + 1
for i in range(M):
    B[i] = bisect_left(C, B[i]) + 1
print(*A)
print(*B)
