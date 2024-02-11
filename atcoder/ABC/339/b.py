H, W, N = map(int, input().split())
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
field = [["."] * W for _ in range(H)]
cur_x, cur_y = 0, 0
cur_dir = 0
for _ in range(N):
    if field[cur_y][cur_x] == ".":
        field[cur_y][cur_x] = "#"
        cur_dir = (cur_dir + 1) % 4
    else:
        field[cur_y][cur_x] = "."
        cur_dir = (cur_dir + 3) % 4
    cur_x += directions[cur_dir][0]
    cur_x %= W
    cur_y += directions[cur_dir][1]
    cur_y %= H
for row in field:
    print(*row, sep="")
