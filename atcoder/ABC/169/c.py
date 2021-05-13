from decimal import ROUND_FLOOR, Decimal

A, B = input().split()
A, B = Decimal(A), Decimal(B)
ans = A * B
print(int(ans))
