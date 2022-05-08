H, W = map(lambda x: int(x)-1, input().split())
R, C = map(lambda x: int(x)-1, input().split())

ans = 0
for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    if 0 <= R+dh <= H and 0 <= C+dw <= W:
        ans += 1
print(ans)
