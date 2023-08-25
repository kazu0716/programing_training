from collections import defaultdict

N = int(input())
cnt = [0] * N
number_set = [set()] * N
for i in range(N):
    cnt[i] += int(input())
    number_set[i] = set(map(int, input().split()))
X = int(input())
ans = defaultdict(list)
for i in range(N):
    if X in number_set[i]:
        ans[cnt[i]].append(i + 1)
if ans:
    key = min(ans)
    print(len(ans[key]))
    print(*ans[key])
else:
    print(0)
    print("")
