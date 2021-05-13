from itertools import combinations

N = int(input())
L = list(map(int, input().split()))
ans = 0

for i, j, k in combinations(range(N), 3):
    if i >= j or j >= k:
        continue
    l = [L[i], L[j], L[k]]
    if len(l) != len(set(l)):
        continue
    l.sort()
    if abs(l[0]-l[1]) < l[2] and l[2] < l[0] + l[1]:
        ans += 1

print(ans)
