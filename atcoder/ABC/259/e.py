from collections import defaultdict

N = int(input())
lcms, cnt, p_max_e = [], defaultdict(int), defaultdict(int)
for _ in range(N):
    m, lcm = int(input()), []
    for _ in range(m):
        p, e = map(int, input().split())
        cnt[(p, e)] += 1
        p_max_e[p] = max(p_max_e[p], e)
        lcm.append((p, e))
    lcms.append(lcm)
ans = set()
for lcm in lcms:
    s = set()
    for p, e in lcm:
        if cnt[(p, e)] == 1 and p_max_e[p] == e:
            s.add((p, e))
    if s:
        ans.add(frozenset(s))
print(len(ans) if len(ans) == N else len(ans)+1)
