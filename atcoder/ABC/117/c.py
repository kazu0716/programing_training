N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))
if N >= M:
    print(0)
    exit()
dis = sorted([X[i + 1] - X[i] for i in range(M - 1)])
ans = X[-1] - X[0]
for _ in range(min(len(dis), N - 1)):
    ans -= dis.pop()
print(ans)
