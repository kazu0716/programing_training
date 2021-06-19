N = int(input())


def check(bits):
    cnt = 0
    for bit in bits:
        if bit == "0":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False

    if cnt == 0:
        return True
    else:
        return False


def solve():
    if N % 2 == 1:
        return
    for i in range(2 ** N):
        bit = bin(i)[2:].rjust(N, "0")
        if check(bit):
            print(bit.replace("0", "(").replace("1", ")"))
    return


solve()
