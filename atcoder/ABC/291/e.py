from collections import deque

N, M = map(int, input().split())
if M < N - 1:
    print("No")
    exit()
graph = [set() for _ in range(N)]
in_cnt = [0] * N
for _ in range(M):
    X, Y = map(int, input().split())
    # NOTE: Avoid to add in_cnt as it is possible to exist some same edges
    if Y - 1 not in graph[X - 1]:
        in_cnt[Y - 1] += 1
        graph[X - 1].add(Y - 1)
# NOTE topological sort by BFS
deq = deque([i for i in range(N) if in_cnt[i] == 0])
topology = []
while deq:
    cur = deq.popleft()
    topology.append(cur)
    for nxt in graph[cur]:
        in_cnt[nxt] -= 1
        if in_cnt[nxt] == 0:
            deq.append(nxt)
# NOTE: judge DAG or not
if len(topology) != N:
    print("No")
    exit()
ans = [0] * N
for i, t in enumerate(topology):
    # NOTE: judge if this node is connected with next node or not
    if i < N - 1 and topology[i + 1] not in graph[t]:
        print("No")
        exit()
    ans[t] = i + 1
print("Yes")
print(*ans)
