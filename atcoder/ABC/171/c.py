N = int(input())


def solve(n):
    if n <= 26:
        return chr(96 + n)
    elif n % 26 == 0:
        return solve(n // 26 - 1) + "z"
    else:
        return solve(n // 26) + chr(96 + n % 26)


print(solve(N))
