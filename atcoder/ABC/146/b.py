N = int(input())
S = input()

ans = ""

for i in range(len(S)):
    n = (ord(S[i])+N)
    if n > 90:
        n = 64 + n % 90
    ans += chr(n)

print(ans)
