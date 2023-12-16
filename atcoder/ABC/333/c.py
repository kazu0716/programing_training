from itertools import combinations_with_replacement

N = int(input())
repunits = [int("1" * i) for i in range(1, 13)]
trio_set = set([sum(r) for r in combinations_with_replacement(repunits, 3)])
print(sorted(list(trio_set))[N-1])
