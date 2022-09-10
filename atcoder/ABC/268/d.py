from itertools import combinations_with_replacement, permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set([input() for _ in range(M)])
length, spaces = sum([len(s) for s in S]), set()
for p in combinations_with_replacement(range(1, 16-length), N-1):
    if sum(p) <= 16-length:
        for pp in permutations(p):
            if pp not in spaces and len(pp) == N-1:
                spaces.add(pp)
for s in permutations(S):
    for space in spaces:
        txt = s[0]
        for i in range(1, N):
            txt += "_" * space[i-1] + s[i]
        if txt not in T and len(txt) >= 3 and len(txt) <= 16:
            print(txt)
            exit()
print(-1)
