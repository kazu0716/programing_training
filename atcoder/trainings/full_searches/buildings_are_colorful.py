N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = float("inf")

for i in range(2**N):
    bit, base, c = bin(i)[2:].rjust(N, "0"), A[0], 0
    if bit.count("1") >= K:
        for i, b in enumerate(list(bit)):
            if b == "1" and i != 0:
                if base >= A[i]:
                    c += base + 1 - A[i]
                    base += 1
            base = max(base, A[i])
        ans = min(ans, c)

print(ans)
