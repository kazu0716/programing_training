from bisect import bisect_left


def get_accum_idx(i):
    if i % 2 == 0:
        return i // 2 - 1
    return (i - 1) // 2


N = int(input())
A = list(map(int, input().split()))
sleep_time = [0]
sleep_list = []
for i in range(N - 1):
    if i % 2 == 0:
        continue
    sleep_time.append(sleep_time[-1] + A[i + 1] - A[i])
    sleep_list.append((A[i], A[i + 1]))
Q = int(input())
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    l_idx, r_idx = bisect_left(A, l), bisect_left(A, r)
    if r_idx % 2 == 1:
        r_idx -= 1
    if l_idx == 0:
        l_idx += 1
    if l_idx % 2 == 0 and l == A[l_idx]:
        l_idx += 1
    l_idx_accum, r_idx_accum = get_accum_idx(l_idx), get_accum_idx(r_idx)
    sleep = sleep_time[r_idx_accum + 1] - sleep_time[l_idx_accum]
    if l_idx % 2 == 0 and l < A[l_idx]:
        sleep -= l - sleep_list[l_idx_accum][0]
    if r_idx % 2 == 0 and r < A[r_idx]:
        sleep -= sleep_list[r_idx_accum][1] - r
    ans.append(sleep)
print(*ans, sep="\n")
