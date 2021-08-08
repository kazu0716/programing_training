from heapq import heappop, heappush

N = int(input())
edges = [[] for _ in range(N)]

for _ in range(N-1):
    A, B = map(int, input().split())
    heappush(edges[A-1], B-1)
    heappush(edges[B-1], A-1)

pre, stack, ans = -1, [0], []

while stack:
    cur = stack[-1]
    if not edges[cur]:
        ans.append(stack.pop()+1)
        continue
    next = heappop(edges[cur])
    if pre == next and len(edges[cur]) > 0:
        tmp = next
        next = heappop(edges[cur])
        heappush(edges[cur], tmp)
    stack.append(next)
    pre = cur

print(*ans[::-1])
