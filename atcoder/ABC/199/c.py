N = int(input())
S = input()
Q = int(input())

rep = False
ans = list(S)

for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 2:
        rep = not rep
    else:
        if rep:
            if A <= N and B <= N:
                i, j = N+A-1, N+B-1
                a, b = ans[i], ans[j]
                ans[i], ans[j] = b, a
            if A <= N and B > N:
                i, j = N+A-1, B-N-1
                a, b = ans[i], ans[j]
                ans[i], ans[j] = b, a
            elif A > N and B > N:
                i, j = A-N-1, B-N-1
                a, b = ans[i], ans[j]
                ans[i], ans[j] = b, a
        else:
            a, b = ans[A-1], ans[B-1]
            ans[A-1], ans[B-1] = b, a

if rep:
    ans = ans[N:]+ans[0:N]

print(*ans, sep="")
