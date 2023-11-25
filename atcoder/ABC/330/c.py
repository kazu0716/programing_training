from bisect import bisect_left

D = int(input())
powers = []
i = 0
while i ** 2 <= D:
    powers.append(i ** 2)
    i += 1
ans = pow(10, 18)
for x in powers:
    i = bisect_left(powers, abs(x - D))
    for y in [powers[j] for j in range(i - 1, i + 2) if 0 <= j < len(powers)]:
        ans = min(ans, abs(x + y - D))
print(ans)
