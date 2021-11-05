N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = [A[i+1]-A[i] for i in range(N-1)]

cnt, ans = 1, 0
while K > 0:
    if A:
        a = A.pop()
    else:
        break
    if B:
        n = B.pop()
    else:
        n = a

    if n*cnt >= K:
        p, q = divmod(K, cnt)
        b = a-p+1
        ans += cnt*p*(a+b)//2
        ans += (b-1)*q
        break
    else:
        b = a-n+1
        ans += cnt*n*(a+b)//2
        K -= n*cnt
        cnt += 1

print(ans)
