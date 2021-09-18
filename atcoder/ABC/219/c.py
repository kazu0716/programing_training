X = list(input())
N = int(input())

tmp, ans = [], []

for _ in range(N):
    S = input()
    string = [chr(97 + X.index(s)) for s in S]
    tmp.append("".join(string))

tmp.sort()

for i in range(len(tmp)):
    s = tmp[i]
    string = [X[(ord(c)-97)] for c in s]
    ans.append("".join(string))

print(*ans, sep="\n")
