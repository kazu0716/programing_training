N, M = map(int, input().split())
inf = pow(10, 18)
d = [[inf] * N for i in range(N)]
ans = 0

for i in range(N):
    d[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    d[a - 1][b - 1] = c

for k in range(N):
    nxt = [[inf] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            nxt[i][j] = min(d[i][j], d[i][k] + d[k][j])
            if nxt[i][j] < inf:
                ans += nxt[i][j]
    d = nxt
print(ans)
