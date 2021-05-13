K = int(input())

ans = -1
A = [0]


for n in range(1, K+1):
    a = 10*A[n-1] + 7
    q = a % K
    A.append(q)
    if q == 0:
        ans = n
        break

print(ans)
