N = int(input())
A = list(map(int, input().split()))

ans = pow(2, 30)


def get_or(l):
    x = l.pop(0)
    for i in l:
        x = x | i
    return x


def get_xor(l):
    x = l.pop(0)
    for i in l:
        x = x ^ i
    return x


for i in range(1, 2 ** (N-1)):
    L = [0]
    bit = bin(i)[2:].rjust(N-1, "0")
    for j, b in enumerate(list(bit)):
        if b == "1":
            L.append(j+1)
    L.append(len(A))
    O = []
    for k in range(1, len(L)):
        O.append(get_or(A[L[k-1]:L[k]]))
    ans = min(ans, get_xor(O))

if len(A) == 1:
    print(A[0])
else:
    print(ans)
