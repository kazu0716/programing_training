N = int(input())
S, T = [], []


def set_points(l):
    min_x, max_x, min_y, max_y = 300, -1, 300, -1
    for i in range(N):
        s = list(input())
        for j in range(len(s)):
            if s[j] == "#":
                l.append([j, i])
                min_x = min(min_x, j)
                max_x = max(max_x, j)
                min_y = min(min_y, i)
                max_y = max(max_y, i)
    return min_x, max_x, min_y, max_y


def convert(l, min_x, max_x, min_y, max_y):
    shape = [[0] * (max_x - min_x + 1)
             for _ in range((max_y - min_y + 1))]
    for x, y in l:
        x -= min_x
        y -= min_y
        shape[y][x] = 1
    return shape


min_xs, max_xs, min_ys, max_ys = set_points(S)
min_xt, max_xt, min_yt, max_yt = set_points(T)

s = convert(S, min_xs, max_xs, min_ys, max_ys)
t = convert(T, min_xt, max_xt, min_yt, max_yt)

flag = False
for _ in range(4):
    if s == t:
        flag = True
        break
    s = list(map(list, zip(*s[::-1])))

if flag:
    print("Yes")
else:
    print("No")
