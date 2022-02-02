N, Q = map(int, input().split())
A = list(map(int, input().split()))
B, S = [], 0
ans = []
for i in range(N-1):
    B.append(A[i]-A[i+1])
    S += abs(A[i]-A[i+1])
for _ in range(Q):
    L, R, V = map(int, input().split())
    L -= 1
    R -= 1
    if L-1 >= 0:
        S += abs(B[L-1]-V)-abs(B[L-1])
        B[L-1] -= V
    if R < N-1:
        S += abs(B[R]+V)-abs(B[R])
        B[R] += V
    ans.append(S)
print(*ans, sep="\n")
