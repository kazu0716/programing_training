N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
mx_a, mx_b, mx_diff = 0, 0, 0
for a, b in AB:
    if b - a >= mx_diff:
        mx_a, mx_b, mx_diff = a, b, b - a
ans = mx_b
encounted = False
for a, b in sorted(AB, reverse=True):
    if not encounted and a == mx_a and b == mx_b:
        encounted = True
        continue
    ans += a
print(ans)
