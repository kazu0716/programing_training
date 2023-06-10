H, W = map(int, input().split())
INF = pow(10, 18)
cookie = set()
a, b, c, d = INF, 0, INF, 0
for i in range(H):
    for j, s in enumerate(input()):
        if s == "#":
            a, b, c, d = min(i, a), max(i, b), min(j, c), max(j, d)
            cookie.add((i, j))
for i in range(a, b + 1):
    for j in range(c, d + 1):
        if (i, j) not in cookie:
            print(i + 1, j + 1)
            exit()
