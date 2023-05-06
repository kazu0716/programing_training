N, M, C = map(int, input().split())
B = tuple(map(int, input().split()))
ans = 0
for _ in range(N):
    A = tuple(map(int, input().split()))
    s = C
    for i in range(M):
        s += A[i] * B[i]
    if s > 0:
        ans += 1
print(ans)
