N = int(input())
A = list(map(int, input().split()))

ans = []

for i in range(len(A)):
    if i % 2 == 0:
        ans.append(max(A))
    else:
        ans.append(-max(A))

    A.remove(max(A))

print(sum(ans))
