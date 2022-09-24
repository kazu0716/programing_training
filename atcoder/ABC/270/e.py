def get_num_eaten_apples(turn_num: int) -> int:
    s = 0
    for a in A:
        s += min(a, turn_num)
    return s


N, K = map(int, input().split())
A = list(map(int, input().split()))
low, high = 0, pow(10, 18)
while high - low > 1:
    mid = (low + high) // 2
    if get_num_eaten_apples(mid) < K:
        low = mid
    else:
        high = mid
for i, a in enumerate(A):
    d = min(high-1, a)
    A[i] -= d
    K -= d
for i in range(N):
    if K <= 0:
        break
    if A[i] <= 0:
        continue
    K -= 1
    A[i] -= 1
print(*A)
