from collections import defaultdict

N = int(input())
lcm, nums, cnt, pe = defaultdict(int), [], defaultdict(int), defaultdict(list)
for _ in range(N):
    m = int(input())
    tmp = []
    for _ in range(m):
        p, e = map(int, input().split())
        cnt[(p, e)] += 1
        tmp.append((p, e))
        pe[p].append(e)
        if p not in lcm or (p in lcm and lcm[p] < e):
            lcm[p] = e
    nums.append(tmp)
for p in pe:
    pe[p].sort()
ans = set()
for num in nums:
    tmp = set()
    for p, e in num:
        if cnt[(p, e)] == 1 and lcm[p] == e:
            if len(pe[p]) > 1:
                e2 = pe[p][-2]
                tmp.add((p, e-e2))
            else:
                tmp.add((p, e))
    if len(tmp) > 0:
        ans.add(frozenset(tmp))
print(len(ans) if len(ans) == N else len(ans)+1)
