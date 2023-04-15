Q = int(input())
MOD = 998244353
n, s, pos = 1, [1], 0
ans = []
for i in range(Q):
    query = input().split()
    if query[0] == "1":
        x = int(query[1])
        n = (n * 10 + x) % MOD
        s.append(x)
    elif query[0] == "2":
        n = (n - s[pos] * pow(10, len(s) - 1 - pos, MOD)) % MOD
        pos += 1
    else:
        ans.append(n)
print(*ans, sep="\n")
