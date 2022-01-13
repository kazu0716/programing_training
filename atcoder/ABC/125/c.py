from math import gcd

N = int(input())
A = list(map(int, input().split()))

gl, gr = A[0], A[-1]
sl, sr = [gl], [gr]
for i in range(1, N):
    gl, gr = gcd(gl, A[i]), gcd(gr, A[-i-1])
    sl.append(gl)
    sr.append(gr)

ans = max(sl[-2], sr[-2])
for i in range(N-1):
    ans = max(ans,  gcd(sl[i], sr[N-3-i]))
print(ans)
