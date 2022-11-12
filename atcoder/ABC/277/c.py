from collections import defaultdict, deque

N = int(input())
edge = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)
deq, visited = deque([1]), set([1])
while deq:
    cur = deq.popleft()
    for nxt in edge[cur]:
        if nxt not in visited:
            deq.append(nxt)
            visited.add(nxt)
print(max(visited))
