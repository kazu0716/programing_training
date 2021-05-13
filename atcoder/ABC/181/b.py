from math import ceil

N = int(input())

ans = 0

for _ in range(N):
    A, B = map(int, input().split())
    s = A + B
    c = B - A + 1
    if c % 2 == 0:
        ans += s * ceil(c/2)
    else:
        ans += s * (ceil(c/2)-1) + ceil(s/2)

print(ans)
