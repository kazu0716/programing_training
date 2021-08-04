N, X = map(int, input().split())
L = list(map(int, input().split()))

d, cnt = 0, 1

for i in range(N):
    d += L[i]
    if X >= d:
        cnt += 1

print(cnt)
