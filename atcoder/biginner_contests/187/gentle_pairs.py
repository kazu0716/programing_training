from itertools import combinations

N = int(input())
P = []
ans = 0

for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

for i in combinations(range(N), 2):
    p1, p2 = P[i[0]], P[i[1]]
    a = abs(p2[1]-p1[1])/abs(p2[0]-p1[0])
    if a <= 1:
        ans += 1

print(ans)
