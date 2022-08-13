from collections import defaultdict

S = list(input())
target, pos, ans = "atcoder", defaultdict(int),  0
for i, s in enumerate(target):
    pos[s] = i
while "".join(S) != target:
    for i in range(len(S)-1):
        cur, nxt = S[i], S[i+1]
        if pos[cur] > pos[nxt]:
            S[i], S[i+1] = nxt, cur
            ans += 1
print(ans)
