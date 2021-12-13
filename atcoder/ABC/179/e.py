from itertools import accumulate

N, X, M = map(int, input().split())
edge = [-1]*M

A = [X]
for i in range(2*M):
    nxt = (A[i]**2) % M
    if edge[nxt] != -1 or nxt == A[i]:
        idx = A.index(nxt)
        break
    edge[A[i]] = nxt
    A.append(nxt)

s = list(accumulate(A))
q, r = divmod(N-idx, len(s)-idx)
if q == 0:
    ans = s[N-1]
elif idx == 0:
    ans = s[-1]*q if r == 0 else s[-1]*q+s[r-1]
else:
    ans = s[idx-1]+(s[-1]-s[idx-1])*q+(s[idx-1+r]-s[idx-1])
print(ans)
