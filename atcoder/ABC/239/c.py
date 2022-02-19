x1, y1, x2, y2 = map(int, input().split())
d = (x1-x2)**2 + (y1-y2)**2
if d <= 20:
    p1, p2 = set([]), set([])
    for dx, dy in ((2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)):
        p1.add((x1+dx, y1+dy))
        p2.add((x2+dx, y2+dy))
    if p1 & p2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
