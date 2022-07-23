def int_to_bits(n: int) -> str:
    return bin(n)[2:].rjust(DIGIT, "0")


N, C = map(int, input().split())
DIGIT = 30
X, low, high, ans = list(int_to_bits(C)), 0, pow(2, DIGIT)-1, []
for _ in range(N):
    T, A = map(int, input().split())
    if T == 1:
        low &= A
        high &= A
    elif T == 2:
        low |= A
        high |= A
    else:
        low ^= A
        high ^= A
    low_bits, high_bits = int_to_bits(low), int_to_bits(high)
    X = [low_bits[i] if b == "0" else high_bits[i] for i, b in enumerate(X)]
    ans.append(int("".join(X), 2))
print(*ans, sep="\n")
