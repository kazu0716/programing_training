from sys import setrecursionlimit

from pypyjit import set_param

set_param("max_unroll_recursion=-1")
setrecursionlimit(pow(10, 9))


def dfs(cur, dis):
    global ans

    for nxt in range(N):
        if dist[cur][nxt] < 0 or nxt in visited:
            continue
        ans = max(ans, dis + dist[cur][nxt])
        visited.add(nxt)
        dfs(nxt, dis + dist[cur][nxt])
        visited.discard(nxt)


N, M = map(int, input().split())
dist = [[-1] * N for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    dist[A - 1][B - 1] = C
    dist[B - 1][A - 1] = C
ans = 0
for root in range(N):
    visited = set([root])
    dfs(root, 0)
print(ans)
