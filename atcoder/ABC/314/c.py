from collections import defaultdict

N, M = map(int, input().split())
S = input()
C = tuple(map(int, input().split()))
colors = defaultdict(list)
for i, c in enumerate(C):
    colors[c].append(i)
ans = [""] * N
for c in range(1, M + 1):
    length = len(colors[c])
    for i in range(length):
        ans[colors[c][i]] = S[colors[c][(length - 1 + i) % length]]
print(*ans, sep="")
