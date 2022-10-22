from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal

A, B = map(int, input().split())
print(Decimal(str(B/A)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
