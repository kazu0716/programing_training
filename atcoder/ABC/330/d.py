N = int(input())
row = [0] * N
col = [0] * N
targets = []
for i in range(N):
    S = input()
    for j, s in enumerate(S):
        if s == "o":
            row[i] += 1
            col[j] += 1
            targets.append((i, j))
ans = 0
for i, j in targets:
    ans += (row[i] - 1) * (col[j] - 1)
print(ans)
