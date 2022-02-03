from statistics import median

N = int(input())
x, y = [], []
p = []
for _ in range(N):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)
    p.append((X, Y))
x.sort()
y.sort()
mx, my = median(x), median(y)
ans = 0
for x, y in p:
    ans += abs(x-mx)+abs(y-my)
print(int(ans))
