from itertools import combinations

N, M = map(int, input().split())
ret, solve = [], int("1" * M, 2)
for _ in range(N):
    S = input()
    n = 0
    for i, s in enumerate(S):
        if s == "o":
            n += pow(2, M - i - 1)
    ret.append(n)
ans = 0
for n1, n2 in combinations(ret, 2):
    if n1 | n2 == solve:
        ans += 1
print(ans)
