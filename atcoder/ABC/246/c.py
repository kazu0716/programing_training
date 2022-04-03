N, K, X = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)

for i in range(N):
    if K == 0:
        break
    if K < A[i]//X:
        A[i] -= X*K
        K = 0
        break
    K -= A[i] // X
    A[i] = A[i] % X
A.sort(reverse=True)
for i in range(N):
    if K == 0:
        break
    if A[i] == 0:
        continue
    A[i] = 0
    K -= 1
print(sum(A))
