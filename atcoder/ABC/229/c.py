N, W = map(int, input().split())
cheese = []

for _ in range(N):
    A, B = map(int, input().split())
    cheese.append((A, B))

cheese.sort()
ans, w = 0, 0

for _ in range(N):
    A, B = cheese.pop()
    if W - w <= B:
        ans += A*(W-w)
        break
    else:
        ans += A*B
        w += B

print(ans)
