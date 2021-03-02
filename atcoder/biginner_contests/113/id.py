from bisect import bisect_left

N, M = map(int, input().split())
ans, Y = [], {}

for _ in range(M):
    p, y = map(int, input().split())
    ans.append((p, y))
    if str(p) in Y:
        Y[str(p)].append(y)
    else:
        Y[str(p)] = [y]

for k in Y:
    Y[k].sort()

for a in ans:
    p, y = a[0], a[1]
    yn = bisect_left(Y[str(p)], y)+1

    print(str(p).rjust(6, "0") + str(yn).rjust(6, "0"))
