N, A, B = map(int, input().split())
q, mod = divmod(N, A+B)

if mod <= A:
    ans = A*q + mod
else:
    ans = A*q + A

print(ans)
