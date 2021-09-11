import numpy as np

N = int(input())
S, T = [], []

min_xs, max_xs, min_ys, max_ys = 300, -1, 300, -1
for i in range(N):
    s = list(input())
    for j in range(len(s)):
        if s[j] == "#":
            S.append([j, i])
            min_xs = min(min_xs, j)
            max_xs = max(max_xs, j)
            min_ys = min(min_ys, i)
            max_ys = max(max_ys, i)

min_xt, max_xt, min_yt, max_yt = 300, -1, 300, -1
for i in range(N):
    t = list(input())
    for j in range(len(t)):
        if t[j] == "#":
            T.append([j, i])
            min_xt = min(min_xt, j)
            max_xt = max(max_xt, j)
            min_yt = min(min_yt, i)
            max_yt = max(max_yt, i)

s_shape = [[0] * (max_xs - min_xs + 1) for _ in range((max_ys - min_ys + 1))]
for s in S:
    x, y = s[0], s[1]
    x -= min_xs
    y -= min_ys
    s_shape[y][x] = 1

s_shape = np.array(s_shape)

t_shape = [[0] * (max_xt - min_xt + 1) for _ in range((max_yt - min_yt + 1))]
for t in T:
    x, y = t[0], t[1]
    x -= min_xt
    y -= min_yt
    t_shape[y][x] = 1

t_shape = np.array(t_shape)

flag = False
for _ in range(4):
    if np.array_equal(s_shape, t_shape):
        flag = True
        break
    s_shape = np.rot90(s_shape)

if flag:
    print("Yes")
else:
    print("No")
