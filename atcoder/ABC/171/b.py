from itertools import accumulate

N, K = map(int, input().split())
P = list(map(int, input().split()))

P.sort()
P_s = list(accumulate(P))
print(P_s[K-1])
