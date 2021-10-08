from collections import deque

H, W = map(int, input().split())
INF = pow(10, 12)

edge = [list(input()) for _ in range(H)]


def bfs(since):
    x, y = since
    deq = deque([(x, y)])
    dis = [[INF] * W for _ in range(H)]
    dis[x][y] = 0
    max_dis = 0
    while deq:
        cur_h, cur_w = deq.popleft()
        for h, w in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            h, w = cur_h + h, cur_w + w
            if 0 <= h and h < H and 0 <= w and w < W:
                if edge[h][w] == "#":
                    continue
                if dis[h][w] != INF:
                    continue
                dis[h][w] = dis[cur_h][cur_w] + 1
                max_dis = max(max_dis, dis[h][w])
                deq.append((h, w))
    return max_dis


ans = 0
for i in range(H):
    for j in range(W):
        if edge[i][j] == "#":
            continue
        ans = max(ans, bfs((i, j)))

print(ans)
