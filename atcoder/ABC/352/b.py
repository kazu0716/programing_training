S = input()
T = input()
i = 0
ans = []
for j, t in enumerate(T):
    if i >= len(S):
        break
    if t == S[i]:
        ans.append(j + 1)
        i += 1
print(*ans)
