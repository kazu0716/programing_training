from itertools import permutations

S = list(input())
ans = set([])

for s1, s2, s3 in permutations(S):
    ans.add("".join([s1, s2, s3]))

print(len(ans))
