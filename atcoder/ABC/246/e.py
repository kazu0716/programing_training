from collections import deque

N = int(input())
AX, AY = map(lambda x: int(x)-1, input().split())
BX, BY = map(lambda x: int(x)-1, input().split())
INF = pow(10, 18)
grid = [tuple(input()) for _ in range(N)]
dist = [[INF]*N for _ in range(N)]
dist[AX][AY] = 0
queue = deque([(AX, AY)])
while queue:
    cur_x, cur_y = queue.popleft()
    cost = dist[cur_x][cur_y] + 1
    for dx, dy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        nxt_x, nxt_y = cur_x + dx, cur_y + dy
        while 0 <= nxt_x < N and 0 <= nxt_y < N and grid[nxt_x][nxt_y] == ".":
            if dist[nxt_x][nxt_y] < cost:
                break
            if dist[nxt_x][nxt_y] > cost:
                queue.append((nxt_x, nxt_y))
                dist[nxt_x][nxt_y] = cost
            nxt_x += dx
            nxt_y += dy
ans = -1 if dist[BX][BY] == INF else dist[BX][BY]
print(ans)
