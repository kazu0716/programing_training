from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = [-1] * N
graph = [set() for _ in range(N)]
for a, b in zip(A, B):
    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)
for i in range(N):
    if X[i] != -1:
        continue
    X[i] = 0
    deq = deque([(i, X[i])])
    while deq:
        cur, v = deq.popleft()
        for nxt in graph[cur]:
            nxt_v = int(not bool(v))
            if X[nxt] == -1:
                X[nxt] = nxt_v
                deq.append((nxt, nxt_v))
            elif X[nxt] != nxt_v:
                exit(print("No"))
print("Yes")
