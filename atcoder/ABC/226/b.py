from collections import defaultdict

N = int(input())
cnt = defaultdict(set)

for _ in range(N):
    length, *line = map(int, input().split())
    cnt[length].add(tuple(line))

ans = 0
for key in cnt:
    ans += len(cnt[key])

print(ans)
