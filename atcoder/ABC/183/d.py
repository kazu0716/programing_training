from itertools import accumulate

N, W = map(int, input().split())
flag = True
data = [0]*(2*pow(10, 5)+1)

for _ in range(N):
    S, T, P = map(int, input().split())
    data[S] += P
    data[T] -= P

for s in accumulate(data):
    if s > W:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
