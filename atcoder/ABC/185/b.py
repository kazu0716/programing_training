N, M, T = map(int, input().split())
events = []

ans, flag, date = N, True, 0

for _ in range(M):
    a, b = map(int, input().split())
    events.append((a, b))

for event in events:
    ans -= event[0] - date
    if ans <= 0:
        flag = False
        break

    ans += event[1] - event[0]
    if ans > N:
        ans = N

    date = event[1]

ans -= T-date
if ans <= 0 and flag:
    flag = False

if flag:
    print("Yes")
else:
    print("No")
