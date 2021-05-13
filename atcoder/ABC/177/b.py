S, T = input(), input()

ans = 10000

for i in range(len(S)-len(T)+1):
    s = S[i:i+len(T)]
    cnt = 0
    for j in range(len(s)):
        if s[j] != T[j]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)
