from bisect import bisect_left


def cast_sleep_time_idx(i):
    """get sleep time index from idx of A"""
    return i // 2 - 1 if i % 2 == 0 else (i - 1) // 2


N = int(input())
A = list(map(int, input().split()))
sleep_time = [0]
for i in range(N - 1):
    if i % 2 == 0:
        continue
    sleep_time.append(sleep_time[-1] + A[i + 1] - A[i])
Q = int(input())
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    l_idx, r_idx = bisect_left(A, l), bisect_left(A, r)
    # NOTE: change idx of getting up at last time
    if r_idx % 2 == 1:
        r_idx -= 1
    # NOTE: change idx of going bed at first time
    if l_idx % 2 == 0 and l == A[l_idx]:
        l_idx += 1
    # NOTE: get total sleep time by cumulative sum
    sleep = sleep_time[cast_sleep_time_idx(r_idx) + 1] - sleep_time[cast_sleep_time_idx(l_idx)]
    # NOTE: decrease surplus sleep time, when l or r is in sleeping time
    if l_idx % 2 == 0 and l < A[l_idx]:
        sleep -= l - A[l_idx - 1]
    if r_idx % 2 == 0 and r < A[r_idx]:
        sleep -= A[r_idx] - r
    ans.append(sleep)
print(*ans, sep="\n")
