N, M = map(int, input().split())
A = list(map(int, input().split()))
is_festival = [False] * (N + 1)
for a in A:
    is_festival[a] = True
rev_festival = is_festival[::-1]
cnt = 0
ans = [0] * (N + 1)
for i, is_fes in enumerate(rev_festival):
    if is_fes:
        cnt = 0
        ans[i] = cnt
    else:
        cnt += 1
        ans[i] = cnt
print(*ans[::-1][1:], sep='\n')
