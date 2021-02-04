n = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n[0])]
b = [int(input()) for i in range(n[1])]

ans = []

for i in a:
    _sum = 0
    for j in range(len(i)):
        _sum += i[j]*b[j]
    ans.append(_sum)

for i in ans:
    print(i)