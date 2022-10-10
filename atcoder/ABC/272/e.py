from math import ceil

N, M = map(int, input().split())
A = tuple(map(int, input().split()))
nums_list = [[] for _ in range(M)]
for i, a in enumerate(A):
    i += 1
    # NOTE: calc range of index number of A[i] between 0 and N
    # index_number = ceil(target_number - a) / i)
    since, until = max(1, ceil((0 - a) / i)), min(M + 1, ceil((N - a) / i))
    # NOTE: append calculated number per count
    for j in range(since, until):
        nums_list[j-1].append(a + i * j)
ans = []
for nums in nums_list:
    min_num, num_set = 0, set(nums)
    while min_num in num_set:
        min_num += 1
    ans.append(min_num)
print(*ans, sep="\n")
