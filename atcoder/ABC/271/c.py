from collections import defaultdict, deque

N = int(input())
cnt, status = 0, defaultdict(bool)
for a in map(int, input().split()):
    if a > N or status[a]:
        cnt += 1
        continue
    status[a] = True
cur = 0
while cnt >= 2:
    if status[cur+1]:
        cur += 1
        continue
    cur += 1
    status[cur] = True
    cnt -= 2
ans, keys = 0, deque(sorted(status.keys()))
while keys:
    if keys[0] != ans + 1 and cnt + len(keys) < 2:
        break
    if keys[0] == ans + 1:
        ans += 1
        keys.popleft()
        continue
    ans += 1
    for _ in range(2-cnt):
        keys.pop()
    if cnt > 0:
        cnt -= 1
print(ans)
