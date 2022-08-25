from collections import defaultdict

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
bonuses = defaultdict(int)
for _ in range(M):
    X, Y = map(int, input().split())
    bonuses[X-1] = Y
for i in range(N-1):
    if i in bonuses:
        T += bonuses[i]
    T -= A[i]
    if T <= 0:
        print("No")
        exit()
print("Yes")
