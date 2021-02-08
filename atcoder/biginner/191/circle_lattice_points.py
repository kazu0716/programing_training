from decimal import Decimal, Context, ROUND_FLOOR, setcontext

# NOTE: sqrtする際の誤差をround_floorで切り捨てるので、微小値を足すことで精度を保つ(多分)
# ref: https://marco-note.net/abc-191-work-log/
C = Context(rounding=ROUND_FLOOR)
setcontext(C)
d = Decimal('1E-9')

X, Y, R = map(Decimal, input().split())
zero = Decimal("0")
ans = 0

for x in range(int(X-R), int(X+R)+1):
    y2_ = R ** 2 - (X-x) ** 2
    if y2_ >= zero:
        y_ = C.sqrt(y2_+d)
        y_min = Y - y_
        y_max = Y + y_
        ans += (int(y_max.quantize(zero)) - int(y_min.quantize(zero)))
print(ans)
