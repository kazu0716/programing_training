from itertools import combinations, permutations

N = list(input())

ans = 0

for i in range(1, len(N)):
    for c in combinations(N, i):
        n = N.copy()
        for j in range(len(c)):
            n.remove(c[j])
        for p1 in permutations(n):
            for p2 in permutations(c):
                a = int("".join(p1))
                b = int("".join(p2))
                if len(p1) == len(str(a)) and len(p2) == len(str(b)):
                    ans = max(ans, a*b)

print(ans)
