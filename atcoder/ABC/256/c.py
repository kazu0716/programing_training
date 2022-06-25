h1, h2, h3, w1, w2, w3 = map(int, input().split())
ans = 0
for n11 in range(1, min(h1, w1)):
    for n21 in range(1, min(h1, w2)):
        for n12 in range(1, min(h2, w1)):
            for n22 in range(1, min(h2, w2)):
                n31, n32, n13, n23 = h1-n11-n21, h2-n12-n22, w1-n11-n12, w2-n21-n22
                if n31 > 0 and n32 > 0 and n13 > 0 and n23 > 0 and w3-n31-n32 == h3-n13-n23 and w3-n31-n32 > 0:
                    ans += 1
print(ans)
