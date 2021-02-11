N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = []

for i in range(len(A)):
    if i % 2 == 0:
        ans.append(A[0])
    else:
        ans.append(-A[0])
    A.pop(0)

print(sum(ans))
