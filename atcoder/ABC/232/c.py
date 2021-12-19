from collections import defaultdict
from itertools import permutations
from sys import exit

N, M = map(int, input().split())
edge1, edge2 = defaultdict(set), defaultdict(set)

for e in (edge1, edge2):
    for _ in range(M):
        A, B = map(int, input().split())
        e[A-1].add(B-1)
        e[B-1].add(A-1)

for dic in permutations(range(N)):
    edge = defaultdict(set)
    for k in edge2:
        edge[dic[k]] = set([dic[v] for v in edge2[k]])
    if edge == edge1:
        print("Yes")
        exit()

print("No")
