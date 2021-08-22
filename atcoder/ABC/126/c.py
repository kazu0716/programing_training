from decimal import Decimal
from math import ceil, log2

N, K = map(Decimal, input().split())

ans = Decimal("0")

if N >= K:
    ans += (N - K + Decimal("1")) / N

for i in range(1, min(int(N)+1, int(K))):
    p = ceil(log2(float(K) / i))
    ans += (Decimal("1") / N) * (Decimal("0.5")) ** Decimal(str(p))

print(ans)
