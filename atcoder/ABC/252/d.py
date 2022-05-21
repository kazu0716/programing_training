from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
keys = sorted(cnt.keys())
s = [0]
for i, k in enumerate(keys):
    s.append(s[i]+cnt[k])
ans = 0
for i in range(1, len(keys)-1):
    mid = keys[i]
    ans += cnt[mid] * s[i] * (s[-1]-s[i+1])
print(ans)
