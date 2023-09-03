from collections import Counter, defaultdict

N = int(input())
A = tuple(map(int, input().split()))
left, right = defaultdict(int), Counter(A)
sum_diff = ans = 0
cnt = defaultdict(int)
# NOTE: ini status
pre_a_j = A[0]
left[pre_a_j] += 1
right[pre_a_j] -= 1
# NOTE: 1 <= j <= N - 2, when A is 0 indexed
for j in range(1, N - 1):
    # NOTE: move right value to center
    right[A[j]] -= 1
    # NOTE: update cnt by pre_a_j and A[j]
    for key in (pre_a_j, A[j]):
        comb_num = left[key] * right[key]
        sum_diff += comb_num - cnt[key]
        cnt[key] = comb_num
    ans += sum_diff - cnt[A[j]]
    # NOTE: move center value to left
    left[A[j]] += 1
    pre_a_j = A[j]
print(ans)
