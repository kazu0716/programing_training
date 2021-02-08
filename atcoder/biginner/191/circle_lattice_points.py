from decimal import Decimal, Context, ROUND_FLOOR, setcontext
from sys import float_info

# NOTE: sqrtする際の誤差をround_floorで切り捨てるので、eで補完する
# ref: https://marco-note.net/abc-191-work-log/
C = Context(rounding=ROUND_FLOOR)
setcontext(C)
# NOTE: pythonの計算機イプシロン
# ref: https://qiita.com/ikuzak/items/1332625192daab208e22
e = Decimal(str(float_info.epsilon))

X, Y, R = map(Decimal, input().split())
zero = Decimal("0")
ans = 0

for x in range(int(X-R), int(X+R)+1):
    y2_ = R ** 2 - (X-x) ** 2
    if y2_ >= zero:
        y_ = C.sqrt(y2_+e)
        y_min = Y - y_
        y_max = Y + y_
        ans += (int(y_max.quantize(zero)) - int(y_min.quantize(zero)))
print(ans)
