N, C = map(int, input().split())
events = []

for _ in range(N):
    a, b, c = map(int, input().split())
    events.append((a-1, c))
    events.append((b, -c))

events.sort()
ans = 0
fee = 0
now = 0

for date, cost in events:
    if date != now:
        ans += min(C, fee) * (date-now)
        now = date
    fee += cost

print(ans)
