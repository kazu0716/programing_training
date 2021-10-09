N, M = map(int, input().split())

A = [list(input()) for _ in range(2*N)]
result = [[i, 0] for i in range(2*N)]


def duel(hand1, hand2):
    if hand1 == hand2:
        return "drew"
    if hand1 == "G" and hand2 == "C":
        return "win"
    if hand1 == "G" and hand2 == "P":
        return "lose"
    if hand1 == "C" and hand2 == "P":
        return "win"
    if hand1 == "C" and hand2 == "G":
        return "lose"
    if hand1 == "P" and hand2 == "G":
        return "win"
    if hand1 == "P" and hand2 == "C":
        return "lose"


for j in range(M):
    for i in range(N):
        k1, k2 = 2*i, 2*i+1
        p1, p2 = result[k1][0], result[k2][0]
        hand1, hand2 = A[p1][j], A[p2][j]
        ret = duel(hand1, hand2)
        if ret == "win":
            result[k1][1] -= 1
        elif ret == "lose":
            result[k2][1] -= 1
    result.sort(key=lambda x: (x[1], x[0]))

ans = []
for i, _ in result:
    ans.append(i+1)

print(*ans, sep="\n")
