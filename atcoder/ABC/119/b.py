from decimal import Decimal

N = int(input())
ans = Decimal("0")
for _ in range(N):
    x, u = input().split()
    ans += Decimal(x) if u == "JPY" else Decimal("380000") * Decimal(x)
print(ans)
