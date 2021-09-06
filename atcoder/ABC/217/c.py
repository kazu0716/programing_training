N = int(input())
P = list(map(int, input().split()))

q = [0] * N

for i in range(N):
    v = i + 1
    q[P[i] - 1] = v

print(*q)
