from collections import defaultdict

N = int(input())
query = []
for _ in range(N):
    t, x = map(int, input().split())
    query.append((t, x))
items = defaultdict(int)
cnt = ans = 0
event = []
for t, x in query[::-1]:
    if t == 1:
        if items[x] < 0:
            cnt -= 1
            items[x] += 1
            event.append(1)
        else:
            event.append(0)
    else:
        items[x] -= 1
        cnt += 1
    ans = max(ans, cnt)
for v in items.values():
    if v < 0:
        exit(print(-1))
print(ans)
print(*event[::-1])
