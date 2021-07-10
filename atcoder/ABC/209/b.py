N, X = map(int, input().split())
A = list(map(int, input().split()))

cost = 0
for i in range(N):
    if (i+1) % 2 == 0:
        cost += A[i] - 1
    else:
        cost += A[i]

if cost <= X:
    print("Yes")
else:
    print("No")
