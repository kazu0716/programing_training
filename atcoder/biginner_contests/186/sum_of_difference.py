N = int(input())
A = list(map(int, input().split()))
S, s = [], 0
ans = 0

A.sort()

for i in range(N):
    s += A[i]
    S.append(s)

for j in range(1, N):
    ans += j*A[j] - S[j-1]

print(ans)
