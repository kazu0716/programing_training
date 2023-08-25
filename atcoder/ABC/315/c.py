from collections import defaultdict

N = int(input())
flavors = defaultdict(list)
for _ in range(N):
    F, S = map(int, input().split())
    flavors[F].append(S)
ans = 0
bests = []
for f in flavors:
    flavors[f].sort()
    if len(flavors[f]) >= 2:
        ans = max(ans, flavors[f][-1] + flavors[f][-2] // 2)
    if flavors[f]:
        bests.append(flavors[f][-1])
if len(bests) >= 2:
    bests.sort()
    ans = max(ans, bests[-1] + bests[-2])
print(ans)
