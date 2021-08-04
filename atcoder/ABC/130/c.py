W, H, x, y = map(int, input().split())

g = (W/2, H/2)

if g[0] == x and g[1] == y:
    print((W * H) / 2, 1)
else:
    print((W * H) / 2, 0)
