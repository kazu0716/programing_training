def is_width_blank(i):
    for j in range(1, W):
        if grid[i][j] == "#":
            return False
    return True


def is_height_blank(j):
    for i in range(1, H):
        if grid[i][j] == "#":
            return False
    return True


H, W = map(int, input().split())
grid = list(list(input()) for _ in range(H))
is_blank = set([])
for i in range(H):
    if grid[i][0] == "#":
        continue
    if is_width_blank(i):
        for j in range(W):
            is_blank.add((i, j))
for j in range(W):
    if grid[0][j] == "#":
        continue
    if is_height_blank(j):
        for i in range(H):
            is_blank.add((i, j))
for i in range(H):
    width = [grid[i][j] for j in range(W) if (i, j) not in is_blank]
    if width:
        print(*width, sep="")
