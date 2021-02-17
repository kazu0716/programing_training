from statistics import median_low

N = int(input())
A, B = [], []
t = 0

for _ in range(N):
    Ai, Bi = map(int, input().split())
    A.append(Ai)
    B.append(Bi)

start = median_low(A)
goal = median_low(B)

for i in range(N):
    t += abs(goal - B[i]) + abs(B[i] - A[i]) + abs(A[i] - start)

print(t)
