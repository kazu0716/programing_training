from sys import setrecursionlimit

from pypyjit import set_param

setrecursionlimit(pow(10, 9))
set_param("max_unroll_recursion=-1")


def dfs(cur, pre):
    # NOTE: append path when end is not Y
    if not ans or ans[-1] != Y:
        ans.append(cur+1)
    if cur == Y-1:
        return
    for nxt in edge[cur]:
        if pre != nxt:
            dfs(nxt, cur)
    # NOTE: pop path when end is not Y
    if ans[-1] != Y:
        ans.pop()


N, X, Y = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N-1):
    U, V = map(int, input().split())
    edge[U-1].append(V-1)
    edge[V-1].append(U-1)
ans = []
dfs(X-1, -1)
print(*ans)
