from collections import defaultdict

N = int(input())
C = list(map(int, input().split()))
min_c, cost = min(C), defaultdict(int)
for i, c in enumerate(C):
    cost[c] = i+1
cnt, ans = N//min_c, []
for _ in range(cnt):
    c_max, i_max = 0, 0
    for c in cost:
        if c + min_c * (cnt-1) <= N and i_max < cost[c]:
            c_max, i_max = c, cost[c]
    if i_max > 0:
        ans.append(i_max)
    N -= c_max
    cnt -= 1
    if min_c * cnt >= N:
        ans += [cost[min_c]] * cnt
        break
print(*ans, sep="")
