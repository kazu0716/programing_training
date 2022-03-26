N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]
B = []
for i in range(M+1):
    s = C[i]
    for j in range(1, N+1):
        if i-j < 0 or i-j >= len(B):
            continue
        s -= A[j]*B[i-j]
    B.append(s//A[0])
print(*B[::-1])
