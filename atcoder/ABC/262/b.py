N, M = map(int, input().split())
edge = [set() for _ in range(N)]
for _ in range(M):
    U, V = map(int, input().split())
    edge[U-1].add(V-1)
    edge[V-1].add(U-1)
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if j in edge[i] and k in edge[j] and i in edge[k]:
                ans += 1
print(ans)
