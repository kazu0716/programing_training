N, K = map(int, input().split())

q, mod = divmod(N, K)

if abs(mod-K) < mod:
    ans = abs(mod-K)
else:
    ans = mod

print(ans)
