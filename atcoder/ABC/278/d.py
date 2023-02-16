from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = {i: defaultdict(int) for i in range(N)}
Q = int(input())
all_inserted, inserted_idx = -1, -1
ans = []
for i in range(Q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        all_inserted, inserted_idx = query[1], i
    elif query[0] == 2:
        B[query[1] - 1][inserted_idx] += query[2]
    else:
        ans.append((A[query[1] - 1] if all_inserted == -1 else all_inserted) + B[query[1] - 1][inserted_idx])
print(*ans, sep="\n")
