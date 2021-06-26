A, B, C, D = map(int, input().split())

blue, red = A, 0
ans = 0

while blue > D*red:
    if B - C*D >= 0:
        ans = -1
        break
    blue += B
    red += C
    ans += 1

print(ans)
