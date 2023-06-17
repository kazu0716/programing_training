from bisect import insort
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
pos_dict = defaultdict(list)
for i, a in enumerate(A):
    insort(pos_dict[a], i + 1)
print(*[j for _, j in sorted([(pos_dict[i][1], i) for i in range(1, N + 1)])])
