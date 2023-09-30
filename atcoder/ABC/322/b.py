N, M = map(int, input().split())
S = input()
T = input()
if S == T[:N] and S == T[M - N:M]:
    ans = 0
elif S == T[:N]:
    ans = 1
elif S == T[M - N:M]:
    ans = 2
else:
    ans = 3
print(ans)
