from sys import setrecursionlimit

setrecursionlimit(pow(10, 9))


def dfs(cur):
    global ans, visited

    if not graph[cur]:
        ans.add(cur)
    for nxt in graph[cur]:
        if nxt in visited:
            continue
        visited.add(nxt)
        dfs(nxt)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B - 1].append(A - 1)
ans = set()
for i in range(N):
    visited = set([i])
    dfs(i)
print(ans.pop() + 1 if len(ans) == 1 else -1)
