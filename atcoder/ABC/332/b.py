K, G, M = map(int, input().split())
g = m = 0
for i in range(K):
    if g >= G:
        g = 0
    elif m <= 0:
        m = M
    else:
        wather = min(m, G - g)
        g += wather
        m -= wather
print(g, m)
