from sys import stdin

r, c = map(int, input().split())
c_sum = [[0]*r for _ in range(c)]

ans = []
last = []
i = 0
_j = range(c)

for _ in range(r):
    l = list(map(int, stdin.readline().split()))
    l.append(sum(l))
    ans.append(l)
    for j in _j:
        c_sum[j][i] = l[j]
    i += 1

for k in c_sum:
    last.append(sum(k))

last.append(sum(last))
ans.append(last)

for l in ans:
    print(" ".join(map(str, l)))
