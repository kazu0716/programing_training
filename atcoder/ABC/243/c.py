from collections import defaultdict
from sys import exit

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
S = input()
counter = defaultdict(lambda: defaultdict(list))
for i in range(N):
    X, Y = P[i]
    d = S[i]
    counter[Y][d].append(X)

for key in counter:
    if "L" not in counter[key] or "R" not in counter[key]:
        continue
    l, r = max(counter[key]["L"]), min(counter[key]["R"])
    if l-r >= 0:
        print("Yes")
        exit()
print("No")
