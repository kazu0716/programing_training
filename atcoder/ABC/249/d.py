from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
counter = defaultdict(int)
for a in A:
    counter[a] += 1
ans = 0
for ai in A:
    aj = 1
    while aj * aj <= ai:
        if ai % aj == 0:
            ans += (1 if aj * aj == ai else 2) * counter[aj] * counter[ai // aj]
        aj += 1
print(ans)
