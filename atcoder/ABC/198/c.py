from math import sqrt

R, X, Y = map(int, input().split())
d = sqrt(X**2 + Y**2)

if d % R == 0:
    print(int(d//R))
else:
    if d > R:
        p = d // R - 1
        print(int(p+2))
    else:
        print(2)
