S = input()

first, letter = [], []
ans = 0
n = len(S)//2
first = list(S[0:n])
letter = list(S[n:])[::-1]

for i in range(n):
    if first[i] != letter[i]:
        ans += 1

print(ans)
