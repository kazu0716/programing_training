from math import factorial

A, B, K = map(int, input().split())

ans = []


def num_of_case(a, b):
    return factorial(a+b)//(factorial(a)*factorial(b))


def gen_strings(a, b, k):
    if a == 0:
        ans.append("b" * (a + b))
    elif b == 0:
        ans.append("a" * (a + b))
    elif num_of_case(a - 1, b) >= k:
        ans.append("a")
        gen_strings(a-1, b, k)
    else:
        ans.append("b")
        gen_strings(a, b-1, k-num_of_case(a-1, b))


gen_strings(A, B, K)

print(*ans, sep="")
