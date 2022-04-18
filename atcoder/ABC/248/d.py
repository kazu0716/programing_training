from bisect import bisect_left, bisect_right
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
hashmap = defaultdict(list)
for i, a in enumerate(A):
    hashmap[a].append(i+1)

Q = int(input())
ans = []
for _ in range(Q):
    L, R, X = map(int, input().split())
    ans.append(bisect_right(hashmap[X], R) - bisect_left(hashmap[X], L))
print(*ans, sep="\n")
