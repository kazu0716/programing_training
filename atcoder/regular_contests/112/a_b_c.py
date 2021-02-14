T = int(input())

for _ in range(T):
    L, R = map(int, input().split())
    n = R - 2*L + 1
    if n > 0:
        print(n*(n+1) // 2)
    else:
        print(0)
