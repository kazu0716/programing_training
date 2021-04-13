n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    u, k, *v = map(int, input().split())
    graph[u] = v

time, find_time, finish_time = 0, [0]*(n+1), [0]*(n+1)


def dfs(v):
    global time

    time += 1
    find_time[v] = time

    for next in graph[v]:
        if find_time[next] == 0:
            dfs(next)
    time += 1
    finish_time[v] = time


for s in range(1, n+1):
    if find_time[s] == 0:
        dfs(s)

for i in range(1, n+1):
    print(i, find_time[i], finish_time[i])
