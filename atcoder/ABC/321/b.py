N, X = map(int, input().split())
A = list(map(int, input().split()))
mi, ma = min(A), max(A)
s = sum(A)
if s - ma >= X:
    print(0)
    exit()
if s - mi >= X:
    print(X - s + mi + ma)
    exit()
print(-1)
