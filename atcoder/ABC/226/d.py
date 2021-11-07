from math import gcd

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
ans = set([])

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        dx, dy = P[i][0]-P[j][0], P[i][1]-P[j][1]
        g = gcd(dx, dy)
        ans.add((dx//g, dy//g))

print(len(ans))
