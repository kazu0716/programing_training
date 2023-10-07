N, M = map(int, input().split())
A = list(map(int, input().split()))
sorted_A = sorted([(a, i) for i, a in enumerate(A)], reverse=True)
score = [0] * N
state = [[False] * M for _ in range(N)]
for i in range(N):
    S = input()
    for j, s in enumerate(S):
        if s == "o":
            score[i] += A[j]
            state[i][j] = True
    score[i] += i + 1
target = max(score)
ans = []
for i in range(N):
    diff = target - score[i]
    cnt = j = 0
    while diff > 0:
        n, k = sorted_A[j]
        if not state[i][k]:
            diff -= n
            cnt += 1
        j += 1
    ans.append(cnt)
print(*ans, sep="\n")
