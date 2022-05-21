from collections import Counter, defaultdict

N = int(input())
cnt = defaultdict(list)
for _ in range(N):
    S = input()
    for i, s in enumerate(S):
        cnt[int(s)].append(i)
for k in cnt:
    cnt[k] = Counter(cnt[k])
ans = pow(10, 18)
for key in cnt:
    k_max, v_max = 0, 0
    for k in cnt[key]:
        if v_max < cnt[key][k]:
            k_max, v_max = k, cnt[key][k]
        elif v_max == cnt[key][k] and k_max < k:
            k_max = k
    ans = min(ans, k_max + 10*(v_max-1))
print(ans)
