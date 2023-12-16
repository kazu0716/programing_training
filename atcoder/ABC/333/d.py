from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 9))
set_param("max_unroll_recursion=-1")


def dfs(cur):
    global cnt

    cnt += 1
    for nxt in edge[cur]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        dfs(nxt)


N = int(input())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)
visited = [False] * N
visited[0] = True
if len(edge[0]) == 1:
    exit(print(1))
cnts = []
for nxt in edge[0]:
    visited[nxt] = True
    cnt = 1
    dfs(nxt)
    cnts.append(cnt)
cnts.sort()
tmp = 0
for i in range(len(edge[0]) - 1):
    tmp += cnts[i]
ans = tmp - (len(edge[0]) - 2)
print(ans)
