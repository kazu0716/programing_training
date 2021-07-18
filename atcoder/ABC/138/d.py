from collections import deque

N, Q = map(int, input().split())
tree = [[] for _ in range(N)]
counter = [0] * N

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

for _ in range(Q):
    p, x = map(int, input().split())
    counter[p-1] += x

finds = [False] * N

queue = deque([0])

while queue:
    v = queue.pop()
    finds[v] = True

    for next in tree[v]:
        if not finds[next]:
            counter[next] += counter[v]
            queue.append(next)

print(*counter)
