from collections import defaultdict, deque

N = int(input())
cnt = defaultdict(set)

for _ in range(N):
    line = deque(list(map(int, input().split())))
    length = line.popleft()
    cnt[length].add(tuple(line))

ans = 0
for key in cnt:
    ans += len(cnt[key])

print(ans)
