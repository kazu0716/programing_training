def is_possible_t(s, t):
    if s == t:
        return True
    if len(s) == len(t):
        cnt = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                cnt += 1
            if cnt > 1:
                return False
        return True
    if abs(len(s) - len(t)) <= 1:
        if len(s) < len(t):
            s, t = t, s
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
            if i - j > 1:
                return False
        return True
    return False


N, T = input().split()
ans = []
for i in range(int(N)):
    S = input()
    if is_possible_t(S, T):
        ans.append(i + 1)
print(len(ans))
print(*ans)
