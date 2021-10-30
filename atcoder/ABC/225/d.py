from collections import deque

N, Q = map(int, input().split())

front, back = [[] for _ in range(N)], [[] for _ in range(N)]
ans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 3:
        x = query[1]-1
        cnt = deque([x+1])
        que1 = back[x].copy()
        while que1:
            cur = que1.pop()
            cnt.append(cur+1)
            if not back[cur]:
                continue
            que1.append(back[cur][-1])
        que2 = front[x].copy()
        while que2:
            cur = que2.pop()
            cnt.appendleft(cur+1)
            if not front[cur]:
                continue
            que2.append(front[cur][-1])
        cnt.appendleft(len(cnt))
        ans.append(cnt)
    else:
        q, x, y = query
        if q == 1:
            front[y-1].append(x-1)
            back[x-1].append(y-1)
        else:
            front[y-1] = []
            back[x-1] = []

for i in range(len(ans)):
    print(*ans[i])
