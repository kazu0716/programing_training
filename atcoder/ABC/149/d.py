N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

ans = 0
actions = [["r", "s", "p"] for _ in range(N)]


def score(t):
    if t == "r":
        return "p", P
    elif t == "s":
        return "r", R
    else:
        return "s", S


for i in range(N):
    t1 = T[i]
    hand, s = score(t1)
    if hand in actions[i]:
        ans += s
        if i + K < N:
            actions[i+K].remove(hand)
    else:
        if i + K >= N:
            continue
        t2 = T[i+K]
        nxt = score(t2)[0]
        idx = actions[i+K].index(nxt)
        del actions[i+K][idx-1]

print(ans)
