V, E = map(int, input().split())
inf = pow(10, 18)
l = [[inf] * V for _ in range(V)]

for i in range(V):
    l[i][i] = 0

for _ in range(E):
    s, t, d = map(int, input().split())
    l[s][t] = d

for k in range(V):
    for i in range(V):
        for j in range(V):
            if l[i][k] == inf or l[k][j] == inf:
                continue
            l[i][j] = min(l[i][j], l[i][k]+l[k][j])

if any(l[i][i] < 0 for i in range(V)):
    print("NEGATIVE CYCLE")
else:
    for i in range(V):
        print(*map(lambda n: n if n < inf else "INF", l[i]))
