K, N = map(int, input().split())
A = list(map(int, input().split()))
A.append(A[0]+K)

ans = 0
diff = 0

for i in range(N):
    d = A[i+1] - A[i]
    diff = max(diff, d)
    ans += d

print(ans - diff)
