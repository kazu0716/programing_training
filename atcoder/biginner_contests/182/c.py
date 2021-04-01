N = input()
k = len(N)

ans = 20

for i in range(1, 2**k):
    bit = bin(i)[2:].rjust(k, "0")
    s = ""
    for j, b in enumerate(bit):
        if b == "1":
            s += str(N)[j]
    if int(s) % 3 == 0:
        ans = min(ans, bit.count("0"))

if ans == 20:
    ans = -1

print(ans)
