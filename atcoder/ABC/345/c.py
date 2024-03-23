from collections import defaultdict

S = input()
cnt = defaultdict(int)
can_make_s = False
for s in S:
    cnt[s] += 1
    if not can_make_s and cnt[s] >= 2:
        can_make_s = True
ans = 0
for k1 in cnt:
    for k2 in cnt:
        if k1 != k2:
            ans += cnt[k1] * cnt[k2]
print(ans // 2 + (1 if can_make_s else 0))
