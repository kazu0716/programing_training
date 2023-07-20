from collections import defaultdict
from itertools import permutations

N, C = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in range(C)]
cnt = {i: defaultdict(int) for i in range(3)}
for i in range(N):
    for j, c in enumerate(map(int, input().split())):
        cnt[(i + j) % 3][c - 1] += 1
ans = pow(10, 18)
for c in permutations(range(C), 3):
    score = 0
    for i in range(3):
        for k, v in cnt[i].items():
            # NOTE: change color from k to c[i]
            score += D[k][c[i]] * v
    ans = min(ans, score)
print(ans)
