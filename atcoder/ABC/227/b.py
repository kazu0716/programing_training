from collections import Counter

N = int(input())
S = Counter(list(map(int, input().split())))

for a in range(1, 1000):
    for b in range(1, 1000):
        s = 4*a*b + 3*a + 3*b
        if s > 1000:
            continue
        if s in S:
            del S[s]

ans = 0
for k in S:
    ans += S[k]

print(ans)
