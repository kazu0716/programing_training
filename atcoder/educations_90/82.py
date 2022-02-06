L, R = map(int, input().split())
MOD = pow(10, 9)+7
ans = 0
for i in range(len(str(L)), len(str(R))+1):
    a = max(L, pow(10, i-1))
    n = min(R, pow(10, i)-1)-a+1
    ans = (ans+i*n*(2*a+n-1)//2) % MOD
print(ans)
