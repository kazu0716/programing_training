from itertools import combinations

N = int(input())
D = list(map(int, input().split()))
ans = 0

for p in combinations(range(N), 2):
    x, y = D[p[0]], D[p[1]]
    ans += x * y

print(ans)
