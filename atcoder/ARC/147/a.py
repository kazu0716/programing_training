from collections import deque

N = int(input())
A = deque(sorted(list(map(int, input().split()))))
ans = 0
while len(A) > 1:
    max_a = A.pop()
    r = max_a % A[0]
    if r > 0:
        A.appendleft(r)
    ans += 1
print(ans)
