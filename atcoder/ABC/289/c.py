N, M = map(int, input().split())
S = []
for _ in range(M):
    _ = int(input())
    S.append(set(map(int, input().split())))
ans, x = 0, set([i + 1 for i in range(N)])
for i in range(2**M):
    bit, s = bin(i)[2:].rjust(M, "0"), set()
    for j, b in enumerate(bit):
        if b == "1":
            s |= S[j]
    if s == x:
        ans += 1
print(ans)
