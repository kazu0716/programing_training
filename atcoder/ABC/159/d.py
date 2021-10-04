from collections import Counter

N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
ans = []


def comb(n):
    if n > 2:
        return n*(n-1)//2
    elif n == 2:
        return 1
    else:
        return 0


s = sum(map(comb, counter.values()))

for i in range(N):
    a = A[i]
    n1, n2 = counter[a], counter[a]-1
    c1, c2 = comb(n1), comb(n2)
    dif = c1-c2
    ans.append(s-dif)

print(*ans, sep="\n")
