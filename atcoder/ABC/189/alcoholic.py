N, X = map(int, input().split())
s, flag = 0.0, True

for i in range(N):
    v, p = map(int, input().split())
    s += v * p
    if s > X*100:
        print(i + 1)
        flag = False
        break

if flag:
    print(-1)
