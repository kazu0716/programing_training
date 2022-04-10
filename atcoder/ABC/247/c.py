from sys import setrecursionlimit

setrecursionlimit(pow(10, 6))


def generate_s(n):
    if n == 1:
        return 1
    return [generate_s(n-1), n, generate_s(n-1)]


N = int(input())
ans = str(generate_s(N)).replace("[", "").replace("]", "").replace(",", "")
print(ans)
