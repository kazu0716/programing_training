N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
MOD = pow(10, 9)+7

ans = 1
for a in A:
    ans = (ans*sum(a)) % MOD
print(ans)
