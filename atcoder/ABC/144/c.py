from math import sqrt

N = int(input())
p = (N, N)

for x in range(1, int(sqrt(N))+1):
    y = N / x
    if y % 1 == 0:
        if p[0] + p[1] >= x + y:
            p = (x, int(y))

print(p[0] + p[1] - 2)
