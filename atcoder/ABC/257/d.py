from collections import defaultdict, deque


def bfs(i, s) -> bool:
    finds, queue = [False]*N, deque([(i, P[i][2])])
    finds[i] = True
    while queue:
        i, p = queue.popleft()
        for d, nxt in dis[i]:
            if d > p*s:
                break
            if finds[nxt]:
                continue
            queue.append((nxt, P[nxt][2]))
            finds[nxt] = True
    return False not in finds


N = int(input())
P = []
for _ in range(N):
    x, y, p = map(int, input().split())
    P.append((x, y, p))
dis = defaultdict(list)
for i in range(len(P)-1):
    for j in range(i+1, len(P)):
        d = abs(P[i][0]-P[j][0]) + abs(P[i][1]-P[j][1])
        dis[i].append((d, j))
        dis[j].append((d, i))
for k in dis:
    dis[k].sort()
limit, ans = max([dis[0][i][0] for i in range(len(dis[0]))]), pow(10, 18)
for i in range(N):
    low, high = 0, limit
    while low <= high:
        mid = (low+high)//2
        if bfs(i, mid):
            high = mid - 1
        else:
            low = mid + 1
    ans = min(ans, high)
print(ans+1)
