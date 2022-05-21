from collections import defaultdict

N = int(input())
cnt = [defaultdict(int) for _ in range(10)]
for _ in range(N):
    S = input()
    for i, s in enumerate(S):
        cnt[int(s)][i] += 1
ans = pow(10, 18)
for i in range(10):
    if not cnt[i]:
        continue
    k_max, v_max = 0, 0
    for k in cnt[i]:
        if v_max < cnt[i][k]:
            k_max, v_max = k, cnt[i][k]
        elif v_max == cnt[i][k] and k_max < k:
            k_max = k
    ans = min(ans, k_max + 10*(v_max-1))
print(ans)
