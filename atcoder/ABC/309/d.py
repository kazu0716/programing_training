from collections import deque


def bfs(root):
    dis[root] = 0
    deq = deque([(root, 0)])
    while deq:
        cur, d = deq.popleft()
        for nxt in edge[cur]:
            if dis[nxt] != -1:
                continue
            dis[nxt] = d + 1
            deq.append((nxt, d + 1))


N1, N2, M = map(int, input().split())
edge = [[] for _ in range(N1 + N2)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
dis = [-1] * (N1 + N2)
bfs(0)
bfs(N1 + N2 - 1)
print(max(dis[:N1]) + max(dis[N1:]) + 1)
