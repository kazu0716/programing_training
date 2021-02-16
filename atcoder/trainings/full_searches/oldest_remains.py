from itertools import combinations

N = int(input())
P = []

for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

P.sort()

C = combinations(P, 2)
ans = 0
st_P = set(P)

for p1, p2 in C:
    x1, y1 = p1
    x2, y2 = p2

    p3 = x1 + y1 - y2, y1 + x2 - x1
    p4 = x2 + y1 - y2, y2 + x2 - x1

    if p3 in st_P and p4 in st_P:
        ans = max((x2 - x1) ** 2 + (y2 - y1) ** 2, ans)

print(ans)
