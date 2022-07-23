from collections import defaultdict

N = int(input())
cnt, ans = defaultdict(int), []
for _ in range(N):
    S = input()
    ans.append(S if S not in cnt else f"{S}({cnt[S]})")
    cnt[S] += 1
print(*ans, sep="\n")
