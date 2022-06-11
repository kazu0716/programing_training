from bisect import bisect_right
from itertools import accumulate

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
S, ans = [0]+list(accumulate(A)), []
for _ in range(Q):
    X = int(input())
    i = bisect_right(A, X)
    ans.append(S[-1]-2*S[i]-N*X+2*i*X)
print(*ans, sep="\n")
