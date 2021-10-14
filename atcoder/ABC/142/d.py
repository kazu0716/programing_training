from collections import deque

A, B = map(int, input().split())
div = set([])

i = 2

while pow(i, 2) <= min(A, B):
    if A % i == 0 and B % i == 0:
        div.add(i)
    if A % i == 0 and B % (A//i) == 0:
        div.add(A//i)
    if B % i == 0 and A % (B//i) == 0:
        div.add(B//i)
    i += 1

if A == B and A > 1:
    div.add(A)

ans = 1
deq = deque(sorted(list(div)))

while deq:
    q = deq.popleft()
    for _ in range(len(deq)):
        p = deq.popleft()
        if p % q != 0:
            deq.append(p)
    ans += 1

print(ans)
