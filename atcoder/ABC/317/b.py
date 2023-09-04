N = int(input())
A = set(map(int, input().split()))
mi = min(A)
for i in range(mi, mi + N + 1):
    if i not in A:
        break
print(i)
