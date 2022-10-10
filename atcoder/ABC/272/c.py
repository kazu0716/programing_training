N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
evens, odds, = [], []
for a in A:
    if a % 2 == 0 and len(evens) < 2:
        evens.append(a)
    elif a % 2 == 1 and len(odds) < 2:
        odds.append(a)
    if len(evens) >= 2 and len(odds) >= 2:
        break
ans = -1
if len(evens) >= 2:
    ans = max(ans, sum(evens))
if len(odds) >= 2:
    ans = max(ans, sum(odds))
print(ans)
