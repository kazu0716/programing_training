from decimal import Decimal

A, B = input().split()
A, B = Decimal(A), Decimal(B)
ans = A * B
print(int(ans))
