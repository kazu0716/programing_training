from collections import deque

N = int(input())
master = [False]*N
A, T = [], []
ans = 0

for _ in range(N):
    deq = deque(list(map(int, input().split())))
    t = deq.popleft()
    T.append(t)
    k = deq.popleft()
    if k == 0:
        A.append([])
    else:
        A.append(list(deq))

ans = 0
stack = [N-1]
while stack:
    cur = stack[-1]
    if not A[cur]:
        stack.pop()
        if master[cur]:
            continue
        master[cur] = True
        ans += T[cur]
    else:
        nxt = A[cur].pop()-1
        if master[nxt]:
            continue
        stack.append(nxt)

print(ans)
