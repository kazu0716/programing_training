import sys
from collections import deque

N, M = map(int, input().split())

edge = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    edge[A-1].append(B-1)
    edge[B-1].append(A-1)

q = deque([0])
routes = [-1] * N

while q:
    cur = q.popleft()
    for nxt in edge[cur]:
        if routes[nxt] != -1:
            continue
        routes[nxt] = cur
        q.append(nxt)

ans = []

for i in range(1, N):
    r = routes[i]
    if r == -1:
        print("No")
        sys.exit(0)
    ans.append(r+1)

print("Yes")
print(*ans, sep="\n")
