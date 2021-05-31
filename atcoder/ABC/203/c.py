N, K = map(int, input().split())

pos = 0
ans = 0
AB = []
for _ in range(N):
    A, B = map(int, input().split())
    AB.append((A, B))

AB = sorted(AB, key=lambda x: x[0])


for A, B in AB:
    if A - pos > K:
        ans = K + pos
        K = 0
        break
    else:
        K = K + B - (A-pos)
        pos = A

if K > 0:
    ans = K + pos

print(ans)
