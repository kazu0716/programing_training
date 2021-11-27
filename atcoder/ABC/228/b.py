N, X = map(int, input().split())
A = tuple(map(int, input().split()))

friends = [False]*N
friends[X-1] = True
que = [A[X-1]-1]
while que:
    cur = que.pop()
    friends[cur] = True
    nxt = A[cur]-1
    if friends[nxt]:
        continue
    friends[nxt] = True
    que.append(nxt)

ans = 0
for friend in friends:
    if friend:
        ans += 1

print(ans)
