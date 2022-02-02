N, K = map(int, input().split())
N = str(N)
for _ in range(K):
    t = 0
    for i in range(len(N)):
        t += int(N[-(i+1)])*pow(8, i)
    s = []
    while t >= 8:
        s.append(str(t % 9))
        t //= 9
    s.append(str(t % 9))
    s = s[::-1]
    N = "".join(s).replace("8", "5")
print(int(N))
