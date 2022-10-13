T = int(input())
ans = []
for _ in range(T):
    N, K = map(int, input().split())
    S = input()
    acm = [[0]*2 for _ in range(N+1)]
    for i in range(N):
        acm[i+1] = acm[i].copy()
        if S[i] != "?":
            acm[i+1][int(S[i])] += 1
    cnt = 0
    for i in range(N-K+1):
        cnt_zero, cnt_one = acm[i+K][0] - acm[i][0], acm[i][1] + (acm[N][1] - acm[i+K][1])
        if cnt_one == cnt_zero == 0:
            cnt += 1
        if cnt > 1:
            break
    ans.append("Yes" if cnt == 1 else "No")
print(*ans, sep="\n")
