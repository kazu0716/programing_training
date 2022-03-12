from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt1, cnt2 = 0, 0
counter = defaultdict(set)
for i in range(N):
    if A[i] == B[i]:
        cnt1 += 1
    counter[B[i]].add(i)
for i in range(N):
    n = len(counter[A[i]])
    cnt2 += n-1 if i in counter[A[i]] else n
print(*(cnt1, cnt2), sep="\n")
