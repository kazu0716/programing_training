from itertools import combinations

N = int(input())
P = []

for _ in range(N):
    X, Y = map(int, input().split())
    P.append((X, Y))

ans = 0
for p1, p2, p3 in combinations(P, 3):
    p1_x, p1_y = p1[0], p1[1]
    p2_x, p2_y = p2[0], p2[1]
    p3_x, p3_y = p3[0], p3[1]
    s = abs((p2_x-p1_x)*(p3_y-p1_y) - (p3_x-p1_x)*(p2_y-p1_y))/2
    if s > 0:
        ans += 1

print(ans)
