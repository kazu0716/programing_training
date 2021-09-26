from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
X = int(input())

cum = list(accumulate(A))
s = cum[-1]

q, mod = divmod(X, s)
cnt = 0
for i in range(N):
    cnt += 1
    if mod < cum[i]:
        break

print(N*q+cnt)
