from copy import deepcopy

N = int(input())
A = [list(input()) for _ in range(N)]
B = deepcopy(A)
B[0] = [A[1][0]] + A[0][:-1]
B[-1] = A[-1][1:] + [A[-2][-1]]
for i in range(1, N - 1):
    B[i][0] = A[i + 1][0]
for i in range(1, N - 1):
    B[i][-1] = A[i - 1][-1]
for i in range(N):
    print(*B[i], sep="")
