N, K = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A)

q, mod = divmod(K, N)
v = B[mod-1]

ans = []
for i in range(N):
    a = A[i]
    if a <= v and mod != 0:
        ans.append(q+1)
    else:
        ans.append(q)

print(*ans, sep="\n")
