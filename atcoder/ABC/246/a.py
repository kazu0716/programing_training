from collections import Counter

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

cnt_x, cnt_y = Counter((x1, x2, x3)), Counter((y1, y2, y3))
x4, y4 = 0, 0
for x in cnt_x:
    if cnt_x[x] == 1:
        x4 = x
        break
for y in cnt_y:
    if cnt_y[y] == 1:
        y4 = y
        break
print(x4, y4)
