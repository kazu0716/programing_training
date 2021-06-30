N = int(input())
S = input()

c, ans = "", 0

for i in range(N):
    if c != S[i]:
        c = S[i]
        ans += 1

print(ans)
