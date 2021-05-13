N, D, H = map(int, input().split())

DH = []
ans = 1000


def calc_slope_intersept(x1, y1, x2, y2):
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    return a, b


for _ in range(N):
    d, h = map(int, input().split())
    DH.append((d, h))

for d1, h1 in DH:
    a, b = calc_slope_intersept(d1, h1, D, H)
    cnt = 0
    for d2, h2 in DH:
        if h2 <= a * d2 + b:
            cnt += 1
    if cnt == len(DH):
        ans = min(b, ans)

if ans > 0:
    print(ans)
else:
    print(0.0)
