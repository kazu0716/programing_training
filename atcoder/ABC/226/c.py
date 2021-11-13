N = int(input())
master = [False]*N
A, T = [], []
ans = 0

for _ in range(N):
    t, k, *a = map(int, input().split())
    T.append(t)
    if k == 0:
        A.append([])
    else:
        A.append(list(a))

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
