N = int(input())
H = list(map(int, input().split()))

pre, cnt, ans = H[0], 0, 0
for i in range(1, N):
    if pre >= H[i]:
        cnt += 1
    else:
        cnt = 0
    ans = max(cnt, ans)
    pre = H[i]

print(ans)
