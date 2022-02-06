from bisect import bisect_left
from math import ceil

K = int(input())
div = set([1, K])
for i in range(2, ceil(pow(K, 1/2))+1):
    if K % i != 0:
        continue
    div.add(i)
    div.add(K//i)
div = sorted(list(div))
ans = 0
for i in range(len(div)):
    for j in range(i, len(div)):
        if div[i]*pow(div[j], 2) > K:
            break
        if K % (div[i]*div[j]) != 0:
            continue
        c = K//(div[i]*div[j])
        idx = bisect_left(div, c)
        if idx >= len(div):
            continue
        if c == div[idx]:
            ans += 1
print(ans)
