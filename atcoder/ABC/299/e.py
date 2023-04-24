from collections import defaultdict, deque

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    edge[u - 1].append(v - 1)
    edge[v - 1].append(u - 1)
K = int(input())
PD = tuple(tuple(map(int, input().split())) for _ in range(K))
white_nodes = set()
black_nodes = defaultdict(set)
for P, D in PD:
    P -= 1
    if D == 0:
        black_nodes[P].add(P)
        continue
    queue = deque([(P, 0)])
    visited = set([P])
    if P not in white_nodes:
        white_nodes.add(P)
    while queue:
        cur, dis = queue.popleft()
        for nxt in edge[cur]:
            if nxt in visited:
                continue
            visited.add(nxt)
            if dis + 1 >= D:
                black_nodes[P].add(nxt)
                continue
            if nxt not in white_nodes:
                white_nodes.add(nxt)
            queue.append((nxt, dis + 1))
for P, D in PD:
    if not black_nodes[P - 1] or black_nodes[P - 1] <= white_nodes:
        print("No")
        exit()
print("Yes")
print(*[1 if i not in white_nodes else 0 for i in range(N)], sep="")
