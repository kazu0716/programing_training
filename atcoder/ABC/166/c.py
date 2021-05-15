N, M = map(int, input().split())
H = list(map(int, input().split()))

routes = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    routes[a-1] = max(routes[a-1], H[b-1])
    routes[b-1] = max(routes[b-1], H[a-1])

ans = 0

for i, route in enumerate(routes):
    if H[i] > route:
        ans += 1

print(ans)
