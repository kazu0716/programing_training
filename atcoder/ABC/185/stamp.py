from math import ceil

N, M = map(int, input().split())
A = list(map(int, input().split()))
D, k = [], pow(10, 18)

A.append(N+1)
A.append(0)
A.sort()

for i in range(len(A)-1):
    dif = A[i+1]-A[i]-1
    if dif > 0:
        k = min(k, dif)
        D.append(dif)

ans = 0

if k == 0:
    ans = 0
elif M == 0:
    ans = 1
else:
    D.sort()
    for d in D:
        ans += ceil(d/k)

print(ans)
