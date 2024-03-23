from collections import defaultdict

H, W, M = map(int, input().split())
TAX = [tuple(map(int, input().split())) for _ in range(M)]
cnt = defaultdict(int)
# NOTE: is_painted[T -> 1 or 2][A -> max(H) or max(W)]
is_painted = [[False] * H, [False] * W]
cnt_t1, cnt_t2 = 0, 0
# NOTE: check these queries in reverse order
for T, A, X in TAX[::-1]:
    if is_painted[T - 1][A - 1]:
        continue
    if T == 1:
        # NOTE: the number of horizontal painted grids depends on the number of already painted rows
        if W - cnt_t2 > 0:
            cnt[X] += W - cnt_t2
        cnt_t1 += 1
    else:
        # NOTE: the number of vertical painted grids depends on the number of already painted columns
        if H - cnt_t1 > 0:
            cnt[X] += H - cnt_t1
        cnt_t2 += 1
    is_painted[T - 1][A - 1] = True
# NOTE: calculate the number of initial state grid(= color number is 0)
cnt_ini = H * W - sum(cnt.values())
if cnt_ini > 0:
    cnt[0] += cnt_ini
print(len(cnt))
for k in sorted(cnt.keys()):
    print(k, cnt[k])
