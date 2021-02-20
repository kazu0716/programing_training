N, K = map(int, input().split())


def g1(x):
    s = list(str(x))
    s.sort(reverse=True)
    return int("".join(s))


def g2(x):
    s = list(str(x))
    s.sort()
    return int("".join(s))


def f(x):
    return g1(x) - g2(x)


a = N

for _ in range(K):
    a = f(a)

print(a)
