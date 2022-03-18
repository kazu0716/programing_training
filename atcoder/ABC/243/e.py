N, M = map(int, input().split())
P, INF = [], pow(10, 18)
dist = [[INF] * N for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    P.append((A-1, B-1, C))
    dist[A-1][B-1] = C
    dist[B-1][A-1] = C

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
ans = 0
for a, b, c in P:
    for k in range(N):
        if dist[a][k]+dist[k][b] <= c:
            ans += 1
            break
print(ans)
