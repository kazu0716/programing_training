N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(A + B)
idx = {n: i + 1 for i, n in enumerate(C)}
for i in range(N):
    A[i] = idx[A[i]]
for i in range(M):
    B[i] = idx[B[i]]
print(*A)
print(*B)
