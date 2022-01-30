from collections import deque

N = int(input())
S = list(input())[::-1]
ans = deque([N])
N -= 1
for s in S:
    if s == "L":
        ans.append(N)
    else:
        ans.appendleft(N)
    N -= 1

print(*ans)
