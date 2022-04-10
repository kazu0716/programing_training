from collections import deque

Q = int(input())
queue = deque([])
ans = []
for _ in range(Q):
    q = tuple(map(int, input().split()))
    if q[0] == 1:
        queue.append((q[1], q[2]))
    else:
        s, cnt = 0, q[1]
        while queue and cnt > 0:
            x, c = queue.popleft()
            if cnt < c:
                s += x*cnt
                queue.appendleft((x, c-cnt))
                cnt = 0
            else:
                s += x*c
                cnt -= c
        ans.append(s)
print(*ans, sep="\n")
