S = list(input())
a, b = map(int, input().split())
a -= 1
b -= 1
aa, bb = S[a], S[b]
S[a], S[b] = bb, aa
print(*S, sep="")
