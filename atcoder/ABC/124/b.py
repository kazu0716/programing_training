N = int(input())
H = tuple(map(int, input().split()))

pre, ans = H[0], 1
for i in range(1, N):
    if pre <= H[i]:
        ans += 1
        pre = H[i]

print(ans)
