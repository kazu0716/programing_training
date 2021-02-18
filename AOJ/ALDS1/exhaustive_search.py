n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

st_M, ans = set(M), ["no"] * q
range_n = range(n)

for i in range(2**n):
    s = 0
    bit = bin(i)[2:].rjust(n, "0")
    for j in range_n:
        b = int(bit[j])
        s += A[j] * b
    if s in st_M:
        for i in [i for i, m in enumerate(M) if m == s]:
            ans[i] = "yes"

print(*ans, sep="\n")
