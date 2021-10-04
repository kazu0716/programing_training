from collections import Counter

N = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
s = sum(map(lambda n: n*(n-1)//2, counter.values()))
ans = []

for i in range(N):
    a = A[i]
    n1, n2 = counter[a], counter[a]-1
    c1, c2 = n1*(n1-1)//2, n2*(n2-1)//2
    diff = c1-c2
    ans.append(s-diff)

print(*ans, sep="\n")
