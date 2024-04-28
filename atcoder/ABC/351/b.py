N = int(input())
A = [tuple(input()) for _ in range(N)]
B = [tuple(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            exit(print(i + 1, j + 1))
