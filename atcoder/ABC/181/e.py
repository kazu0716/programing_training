from bisect import bisect_left

N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))
H.sort()

s1, s2 = [], []
cnt1, cnt2 = 0, 0
for n in range(N//2):
    cnt1 += H[2*n+1]-H[2*n]
    cnt2 += H[2*(n+1)]-H[2*(n+1)-1]
    s1.append(cnt1)
    s2.append(cnt2)

ans = pow(10, 18)
for i in range(M):
    w = W[i]
    if len(H) > 1:
        idx = bisect_left(H, w)
        if idx % 2 == 0:
            diff = H[idx]-w
            n = idx//2-1
        else:
            diff = w-H[idx-1]
            n = (idx-1)//2-1
        if n < 0:
            ret = s2[-1]+diff
        elif n >= N//2-1:
            ret = s1[-1]+diff
        else:
            ret = s2[-1]-s2[n]+s1[n]+diff
    else:
        ret = abs(H[0]-w)
    ans = min(ans, ret)

print(ans)
