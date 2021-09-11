from itertools import combinations

N = int(input())
X, Y = {}, {}

ans = 0

for _ in range(N):
    x, y = map(int, input().split())
    if x in X:
        X[x].add((x, y))
    else:
        X[x] = set([(x, y)])
    if y in Y:
        Y[y].add((x, y))
    else:
        Y[y] = set([(x, y)])

for x in X:
    xset = X[x]
    for p in combinations(xset, 2):
        p1, p2 = p[0], p[1]
        yset = Y[p1[1]]
        yset -= set([p1, p2])
        for p3 in yset:
            if (p3[0], p2[1]) in Y[p2[1]]:
                ans += 1

print(ans)
