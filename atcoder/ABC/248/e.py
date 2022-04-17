from itertools import combinations

N, K = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]
if K == 1:
    print("Infinity")
    exit()
finds, ans = set(), 0
for p1, p2 in combinations(P, 2):
    cnt, p_set = 0, set()
    for x, y in P:
        if (p2[0] - p1[0]) * (y - p1[1]) == (x - p1[0]) * (p2[1] - p1[1]):
            cnt += 1
            p_set.add((x, y))
    if cnt >= K and p_set not in finds:
        ans += 1
        finds.add(frozenset(p_set))
print(ans)
