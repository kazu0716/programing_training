N = int(input())

score1, score2 = [0], [0]
cnt1, cnt2 = 0, 0

for _ in range(N):
    c, p = map(int, input().split())
    if c == 1:
        cnt1 += p
        score1.append(cnt1)
        score2.append(cnt2)
    else:
        cnt2 += p
        score2.append(cnt2)
        score1.append(cnt1)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(score1[r] - score1[l-1], score2[r]-score2[l-1])
