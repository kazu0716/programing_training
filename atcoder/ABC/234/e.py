from bisect import bisect_left
from sys import exit


def check(x):
    x = str(x)
    diff = int(x[0])-int(x[1])
    for i in range(1, len(x)-1):
        if int(x[i])-int(x[i+1]) != diff:
            return False
    return True


X = input()
XX = int(X)
n = len(X)

if n <= 2:
    print(X)
    exit()
if 3 <= n and n <= 5:
    XX = int(X)
    while not check(XX):
        XX += 1
    print(XX)
    exit()

top = int(X[0])
comp = [int(X[0]*n), int(str(top+1)*n)]
if top < 5:
    d = int("".join([str(i) for i in range(top, top+n-1) if i < 10]))
    if check(d):
        comp.append(d)
else:
    for t in (top, top+1):
        d = int("".join([str(i) for i in range(t, t-n, -1) if i >= 0]))
        if check(d):
            comp.append(d)
comp.sort()
print(comp[bisect_left(comp, XX)])
