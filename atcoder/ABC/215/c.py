from itertools import permutations

S, K = input().split()
K = int(K)

ans = set()

for p in permutations(S):
    s = "".join(p)
    ans.add(s)

ans = list(ans)
ans.sort()
print(ans[K-1])
