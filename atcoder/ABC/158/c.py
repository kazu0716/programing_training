from decimal import Decimal

A, B = map(int, input().split())
ans = -1

for i in range(1, int(max(A//0.08, B//0.1))+2):
    d = Decimal(str(i))
    if A == int(d*Decimal("0.08")) and B == int(d*Decimal("0.1")):
        ans = i
        break

print(ans)
