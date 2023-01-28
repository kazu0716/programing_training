from collections import deque

S = input()
T = input()
back = deque(list(S[-len(T):]))
cnt = 0
for i, s in enumerate(S[-len(T):]):
    if T[i] == s or (s == "?" or T[i] == "?"):
        cnt += 1
ans = ["Yes" if cnt == len(T) else "No"]
for x in range(1, len(T) + 1):
    idx = x - 1
    added = S[idx]
    poped = back.popleft()
    if T[idx] == "?":
        pass
    else:
        if poped == "?" or poped == T[idx]:
            cnt -= 1
        if added == "?" or added == T[idx]:
            cnt += 1
    ans.append("Yes" if cnt == len(T) else "No")
print(*ans, sep="\n")
