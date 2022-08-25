H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]
vis = [[False]*W for _ in range(H)]
h, w = 0, 0
while not vis[h][w]:
    vis[h][w] = True
    cmd = G[h][w]
    if cmd == "U" and h > 0:
        h -= 1
    elif cmd == "D" and h < H-1:
        h += 1
    elif cmd == "L" and w > 0:
        w -= 1
    elif cmd == "R" and w < W-1:
        w += 1
    else:
        print(h+1, w+1)
        exit()
print(-1)
