from collections import deque

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
ans = []
Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())
    cnt, finds, queue = x, set([x-1]), deque([(x-1, 0)])
    while queue:
        cur, dis = queue.popleft()
        for nxt in edge[cur]:
            if dis+1 > k or nxt in finds:
                continue
            cnt += nxt+1
            finds.add(nxt)
            queue.append((nxt, dis+1))
    ans.append(cnt)
print(*ans, sep="\n")
