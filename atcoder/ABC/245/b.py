_ = int(input())
A = set(map(int, input().split()))
for i in range(2001):
    if i in A:
        continue
    break
print(i)
