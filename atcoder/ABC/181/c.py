from itertools import combinations

N = int(input())
P = []
flag = False

for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

for c in combinations(P, 3):
    x1, y1 = c[0][0], c[0][1]
    x2, y2 = c[1][0], c[1][1]
    x3, y3 = c[2][0], c[2][1]
    if (x1 == x2 and x2 == x3) or (y1 == y2 and y2 == y3):
        flag = True
        break
    try:
        if (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2):
            flag = True
            break
    except ZeroDivisionError:
        pass

if flag:
    print("Yes")
else:
    print("No")
