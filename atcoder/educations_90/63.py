from collections import defaultdict

H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for n in range(pow(2, H)):
    bit, cnt1 = bin(n)[2:].zfill(H), defaultdict(int)
    for j in range(W):
        cnt2 = defaultdict(int)
        for i, b in enumerate(bit):
            if b == "1":
                cnt2[P[i][j]] += 1
        keys = list(cnt2.keys())
        if len(keys) == 1:
            cnt1[keys[0]] += cnt2[keys[0]]
    for k in cnt1:
        ans = max(ans, cnt1[k])
print(ans)
