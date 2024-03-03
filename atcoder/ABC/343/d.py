from collections import defaultdict

N, T = map(int, input().split())
score = [0] * N
kinds = defaultdict(int)
kinds[0] = N
ans = []
for _ in range(T):
    A, B = map(int, input().split())
    cur = score[A - 1]
    nxt = cur + B
    score[A - 1] = nxt
    kinds[cur] -= 1
    if kinds[cur] <= 0:
        kinds.pop(cur)
    kinds[nxt] += 1
    ans.append(len(kinds.keys()))
print(*ans, sep="\n")
