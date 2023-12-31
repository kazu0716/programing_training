S = list(input())
ans = 1
for i in range(len(S)):
    for j in range(i + 1, len(S)):
        if S[i : j + 1] == S[i : j + 1][::-1]:
            ans = max(ans, j - i + 1)
print(ans)
