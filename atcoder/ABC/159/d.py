from collections import Counter


def comb(n):
    return n*(n-1)//2


N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
s = sum(map(comb, counter.values()))
ans = []

for i in range(N):
    a = A[i]
    n1, n2 = counter[a], counter[a]-1
    c1, c2 = comb(n1), comb(n2)
    diff = c1-c2
    ans.append(s-diff)

print(*ans, sep="\n")
