ans = 0

N = int(input())
A = list(map(float, input().split()))

while True:
    if 1 in map(lambda y: y % 2, A):
        break
    else:
        A = list(map(lambda x: x/2, A))
        ans += 1
print(ans)
