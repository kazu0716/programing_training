N, D = map(int, input().split())

walls = []
for _ in range(N):
    L, R = map(int, input().split())
    walls.append((L, R))
walls.sort(key=lambda x: x[1], reverse=True)

ans = 0
while walls:
    _, r1 = walls.pop()
    ans += 1
    while walls:
        l2, r2 = walls.pop()
        if r1+D-1 >= l2:
            continue
        walls.append((l2, r2))
        break

print(ans)
