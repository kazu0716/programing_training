from bisect import bisect_left


def get_bisect_val(li, idx, is_left):
    return li[idx] if 0 <= idx < len(li) else INF if is_left else -1


A, B, Q = map(int, input().split())
S = sorted([int(input()) for _ in range(A)])
T = sorted([int(input()) for _ in range(B)])
INF = pow(10, 18)
ans = []
for _ in range(Q):
    x = int(input())
    s_idx, t_idx = bisect_left(S, x), bisect_left(T, x)
    sl, sr = get_bisect_val(S, s_idx - 1, True), get_bisect_val(S, s_idx, False)
    tl, tr = get_bisect_val(T, t_idx - 1, True), get_bisect_val(T, t_idx, False)
    d = INF
    if sl < x and tl < x:
        d = min(d, abs(min(sl, tl) - x))
    if x < sr and x < tr:
        d = min(d, abs(max(sr, tr) - x))
    if sl < x < tr:
        d = min(d, min(abs(sl - x), abs(tr - x)) + abs(tr - sl))
    if tl < x < sr:
        d = min(d, min(abs(tl - x), abs(sr - x)) + abs(sr - tl))
    ans.append(d)
print(*ans, sep="\n")
