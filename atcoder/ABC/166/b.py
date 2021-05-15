N, K = map(int, input().split())

sunuke = [False] * N

for _ in range(K):
    d = int(input())
    for a in list(map(int, input().split())):
        sunuke[a-1] = True

ans = 0
for b in sunuke:
    if not b:
        ans += 1

print(ans)
