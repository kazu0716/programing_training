from itertools import combinations

pawns = []
for i in range(9):
    for j, s in enumerate(input()):
        if s == "#":
            pawns.append((i, j))
ans = 0
for c1, c2, c3, c4 in combinations(pawns, 4):
    d1 = (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2
    d2 = (c1[0] - c3[0]) ** 2 + (c1[1] - c3[1]) ** 2
    d3 = (c2[0] - c4[0]) ** 2 + (c2[1] - c4[1]) ** 2
    d4 = (c3[0] - c4[0]) ** 2 + (c3[1] - c4[1]) ** 2
    d5 = (c1[0] - c4[0]) ** 2 + (c1[1] - c4[1]) ** 2
    d6 = (c2[0] - c3[0]) ** 2 + (c2[1] - c3[1]) ** 2
    if d1 == d2 == d3 == d4 and d5 == d6 == 2*d1:
        ans += 1
print(ans)
