N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
graph = [set() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            graph[i].add(j)
            graph[j].add(i)
for g in graph:
    print(*sorted([i + 1 for i in list(g)]))
