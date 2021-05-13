N = int(input())
A = tuple(map(int, input().split()))

ans, ma = 0, 0

for k in range(2, max(A)+1):
    s = 0
    for a in A:
        if a % k == 0:
            s += 1
    if s >= ma:
        ma = s
        ans = k

print(ans)
