N = int(input())
P = list(map(int, input().split()))

cnt = 0

for i in range(1, N-1):
    p1, p2, p3 = P[i-1], P[i], P[i+1]
    if p2 < max(p1, p3) and p2 > min(p1, p3):
        cnt += 1

print(cnt)
