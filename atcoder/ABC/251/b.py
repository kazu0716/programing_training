N, W = map(int, input().split())
A = list(map(int, input().split()))

ans = set()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if A[i]+A[j]+A[k] <= W:
                ans.add(A[i]+A[j]+A[k])
        if A[i]+A[j] <= W:
            ans.add(A[i]+A[j])
    if A[i] <= W:
        ans.add(A[i])
print(len(ans))
