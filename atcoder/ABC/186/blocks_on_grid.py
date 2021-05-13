H, W = map(int, input().split())
m, A, ans = 100, [], 0

for _ in range(H):
    a = list(map(int, input().split()))
    m = min(m, min(a))
    A.append(a)

for i in range(H):
    for j in range(W):
        d = A[i][j] - m
        ans += d

print(ans)
