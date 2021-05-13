S, T = list(input()), list(input())
ans = 0

for i, s in enumerate(S):
    if T[i] == s:
        continue
    ans += 1

print(ans)
