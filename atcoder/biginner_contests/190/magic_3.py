N, S, D = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

flag = False

for xy in XY:
    x, y = xy
    if x < S and y > D:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
