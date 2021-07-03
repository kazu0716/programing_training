N = int(input())
B = list(map(int, input().split()))

pre, ans = pow(10, 6), 0
for i in range(N-2, -1, -1):
    n = B[i]
    ans += min(n, pre)
    pre = n

print(ans+pre)
