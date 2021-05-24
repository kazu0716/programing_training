import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

L = []

ans = 0
for j in range(N):
    L.append(B[C[j]-1])

L.sort()
A.sort()

for i in range(N):
    j = bisect.bisect_left(L, A[i])
    k = bisect.bisect_right(L, A[i])
    ans += k-j

print(ans)
