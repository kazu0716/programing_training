# NOTE: need to submit this solution by python3 not pypy3
from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(pow(10, 9))


def dfs(cur):
    global ans
    if ans >= limit:
        print(limit)
        exit(0)
    for nxt in edge[cur]:
        if not vis[nxt]:
            vis[nxt] = True
            ans += 1
            dfs(nxt)
    vis[cur] = False


N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u - 1].append(v - 1)
    edge[v - 1].append(u - 1)

ans, limit = 1, pow(10, 6)
vis = defaultdict(bool)
vis[0] = True
dfs(0)
print(ans)
