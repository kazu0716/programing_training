from collections import deque


def get_start_point():
    for i in range(H):
        for j in range(W):
            if C[i][j] == "S":
                return i, j


H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
dd = ((1, 0), (0, 1), (-1, 0), (0, -1))
sx, sy = get_start_point()
queue = deque([])
for i, d in enumerate(dd):
    h, w = sx + d[0], sy + d[1]
    if 0 <= h < H and 0 <= w < W and C[h][w] == ".":
        queue.append((h, w, i))
        C[h][w] = i
while queue:
    h, w, i = queue.popleft()
    for dh, dw in dd:
        nxt_h, nxt_w = h + dh, w + dw
        if 0 <= nxt_h < H and 0 <= nxt_w < W:
            if C[nxt_h][nxt_w] not in ("S", ".", i, "#"):
                print("Yes")
                exit()
            if C[nxt_h][nxt_w] == ".":
                queue.append((nxt_h, nxt_w, i))
                C[nxt_h][nxt_w] = i
print("No")
