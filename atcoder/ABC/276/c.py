from bisect import bisect_left

N = int(input())
P = list(map(int, input().split()))
if P[-2] > P[-1]:
    P[-1], P[-2] = P[-2], P[-1]
    print(*P)
    exit()
i, tail = N - 1, [P[-1]]
while i - 1 >= 0 and P[i-1] < P[i]:
    tail.append(P[i-1])
    i -= 1
tail.sort()
idx = bisect_left(tail, P[i-1])
tail[idx-1], P[i-1] = P[i-1], tail[idx-1]
print(*(P[:i] + sorted(tail, reverse=True)))
