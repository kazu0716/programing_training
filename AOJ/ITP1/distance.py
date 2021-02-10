from decimal import Decimal, Context, ROUND_FLOOR, setcontext

C = Context(rounding=ROUND_FLOOR)
setcontext(C)

x1, y1, x2, y2 = map(Decimal, input().split())
r_2 = (x2-x1)**2 + (y2-y1)**2
print(C.sqrt(r_2))
