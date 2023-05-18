N = int(input())
h = list(map(int, input().split()))
ans = 0
while h.count(0) < N:
    l = 0
    while l < len(h):
        if h[l] == 0:
            l += 1
            continue
        r = len(h)
        if 0 in h[l:]:
            r = h.index(0, l, len(h))
        min_h = min(h[l:r])
        for i in range(l, r):
            h[i] -= min_h
        ans += min_h
        l = r + 1
print(ans)
