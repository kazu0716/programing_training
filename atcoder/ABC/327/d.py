from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = [-1] * N
graph: list[set[int]] = [set() for _ in range(N)]
for a, b in zip(A, B):
    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)
for i in range(N):
    if X[i] != -1:
        continue
    X[i] = 0
    deq = deque([(i, X[i])])
    while deq:
        cur, bit = deq.popleft()
        for nxt in graph[cur]:
            if X[nxt] == -1:
                X[nxt] = ~bit & 1
                deq.append((nxt, X[nxt]))
            elif X[nxt] != ~bit & 1:
                exit(print("No"))
print("Yes")
