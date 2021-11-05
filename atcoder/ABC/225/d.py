from collections import deque

N, Q = map(int, input().split())
front, back = [0]*(N+1), [0]*(N+1)
ans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 3:
        x = query[1]
        cnt = deque([x])
        cur = x
        while front[cur] != 0:
            cur = front[cur]
            cnt.appendleft(cur)
        cur = x
        while back[cur] != 0:
            cur = back[cur]
            cnt.append(cur)
        cnt.appendleft(len(cnt))
        ans.append(cnt)
    else:
        q, x, y = query
        if q == 1:
            front[y], back[x] = x, y
        else:
            front[y], back[x] = 0, 0

for i in range(len(ans)):
    print(*ans[i])
