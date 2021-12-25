from bisect import bisect_right
from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

s_dict = defaultdict(list)
cnt, s = 0, []
for i in range(N+1):
    if i > 0:
        cnt += A[i-1]
    s.append(cnt)
    s_dict[cnt].append(i)

ans = 0
for l in range(N):
    sr = K + s[l]
    ans += len(s_dict[sr])-bisect_right(s_dict[sr], l)

print(ans)
