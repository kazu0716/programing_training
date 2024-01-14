N = int(input())
A = list(map(int, input().split()))
cur_l = cur_r = 0
left, right = [], []
for i in range(N):
    left.append(min(cur_l + 1, A[i]))
    right.append(min(cur_r + 1, A[N - 1 - i]))
    cur_l, cur_r = left[-1], right[-1]
right = right[::-1]
print(max([min(left[i], right[i]) for i in range(N)]))
