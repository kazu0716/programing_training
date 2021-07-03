N, K, Q = map(int, input().split())

points = [K] * N
ans = []

for _ in range(Q):
    A = int(input())
    points[A-1] += 1

for i in range(N):
    if points[i] > Q:
        ans.append("Yes")
    else:
        ans.append("No")

print(*ans, sep="\n")
