N = int(input())
S = input()
cnt, n = 0, 0

for i in range(N):
    if S[i] == "(":
        cnt += 1
    else:
        cnt -= 1
    if cnt < 0:
        n += 1

print(n)
