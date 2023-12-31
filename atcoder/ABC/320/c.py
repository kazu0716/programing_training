from itertools import permutations

M = int(input())
INF = pow(10, 9)
S = [input() * 3 for _ in range(3)]
ans = INF
for target in "0123456789":
    for p in permutations(range(3)):
        cur = -1
        for i in p:
            pre, cur = cur, S[i].find(target, cur + 1)
            if cur == -1 or cur <= pre:
                break
        if cur > 0:
            ans = min(ans, cur)
print(ans if ans < INF else -1)
