L, N1, N2 = map(int, input().split())
A1 = [list(map(int, input().split())) for _ in range(N1)][::-1]
A2 = [list(map(int, input().split())) for _ in range(N2)][::-1]
ans = 0
while A1 or A2:
    n1, cnt1 = A1[-1]
    n2, cnt2 = A2[-1]
    if n1 == n2:
        ans += min(cnt1, cnt2)
    if cnt1 == cnt2:
        A1.pop()
        A2.pop()
    elif cnt1 < cnt2:
        A1.pop()
        A2[-1][1] -= cnt1
    else:
        A1[-1][1] -= cnt2
        A2.pop()
print(ans)
