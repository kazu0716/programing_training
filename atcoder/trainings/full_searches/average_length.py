from itertools import permutations
from math import sqrt

N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]

s = 0.0

P = list(permutations(range(N), N))

for p in P:
    d = 0.0
    for i in range(1, len(p)):
        t_i = T[p[i]]
        t_i_1 = T[p[i-1]]
        d_2 = (t_i[0] - t_i_1[0]) ** 2 + (t_i[1] - t_i_1[1]) ** 2
        d += sqrt(d_2)
    s += d

print(s/len(P))
