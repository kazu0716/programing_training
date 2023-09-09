N = int(input())
divisor = [i for i in range(1, 10) if N % i == 0]
ans = []
for i in range(N + 1):
    mi = "-"
    for j in divisor:
        if N % j == 0 and i % (N // j) == 0:
            mi = j
            break
    ans.append(mi)
print(*ans, sep="")
