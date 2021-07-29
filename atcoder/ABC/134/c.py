N = int(input())
A = [int(input()) for _ in range(N)]
B = sorted(A)

for i in range(N):
    if A[i] != B[-1]:
        print(B[-1])
    else:
        print(B[-2])
