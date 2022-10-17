from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
for p in permutations((A[-3:])):
    ans = max(ans, int("".join(map(str, p))))
print(ans)
