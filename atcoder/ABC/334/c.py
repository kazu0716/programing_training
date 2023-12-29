N, K = map(int, input().split())
A = set(map(int, input().split()))
socks = []
for i in range(N):
    socks.append(i)
    if i + 1 not in A:
        socks.append(i)
if len(socks) % 2 == 0:
    ans = 0
    for i in range(0, len(socks), 2):
        ans += socks[i + 1] - socks[i]
    exit(print(ans))
s = [0]
for i in range(0, len(socks) - 1, 2):
    s.append(s[-1] + socks[i + 1] - socks[i])
s_rev = [0]
socks_rev = socks[::-1]
for i in range(0, len(socks_rev) - 1, 2):
    s_rev.append(s_rev[-1] + socks_rev[i] - socks_rev[i + 1])
ans = pow(10, 18)
for i, ss in enumerate(socks):
    if i % 2 == 0:
        ans = min(ans, s[i // 2] + s_rev[len(s_rev) - 1 - i // 2])
        continue
    add = socks[i + 1] - socks[i - 1]
    ans = min(ans, s[i // 2 - 1] + s_rev[len(s_rev) - 2 - i // 2] + add)
print(ans)
