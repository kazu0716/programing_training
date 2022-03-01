from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 6))
set_param("max_unroll_recursion=-1")

N = int(input())
edge = [[] for _ in range(N)]
count, ans = 1, [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)


def dfs(cur, pre):
    global count
    ans[cur] = [count, count]
    for nxt in edge[cur]:
        if nxt == pre:
            continue
        dfs(nxt, cur)
        ans[cur][1] = max(ans[nxt][1], ans[cur][1])
    if ans[cur][1] == count:
        count += 1


dfs(0, -1)
for a in ans:
    print(*a)
