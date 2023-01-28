S = input()
T = input()
cnt = 0
for i, s in enumerate(S[-len(T):]):
    if T[i] == s or (s == "?" or T[i] == "?"):
        cnt += 1
ans = ["Yes" if cnt == len(T) else "No"]
for idx in range(len(T)):
    added, popped = S[idx], S[-len(T) + idx]
    if T[idx] != "?" and (popped == "?" or popped == T[idx]):
        cnt -= 1
    if T[idx] != "?" and (added == "?" or added == T[idx]):
        cnt += 1
    ans.append("Yes" if cnt == len(T) else "No")
print(*ans, sep="\n")
