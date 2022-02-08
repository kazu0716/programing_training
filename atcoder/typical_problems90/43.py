from collections import deque

H, W = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
INF = 10**18
dd = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dist = [[-1 if s == "#" else INF for s in input()] for _ in range(H)]
dist[sx-1][sy-1] = 0
queue = deque([(sx-1, sy-1)])

while queue:
    h, w = queue.popleft()
    d = dist[h][w]+1
    for dh, dw in dd:
        hh = h + dh
        ww = w + dw
        while 0 <= hh < H and 0 <= ww < W and dist[hh][ww] != -1 and dist[hh][ww] >= d:
            dist[hh][ww] = d
            queue.append((hh, ww))
            hh += dh
            ww += dw

print(dist[gx-1][gy-1]-1)
