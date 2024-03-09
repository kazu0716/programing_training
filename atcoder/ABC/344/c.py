_ = int(input())
A = list(map(int, input().split()))
_ = int(input())
B = list(map(int, input().split()))
_ = int(input())
C = sorted(list(map(int, input().split())))
_ = int(input())
X = list(map(int, input().split()))

nums = set()
for a in A:
    for b in B:
        for c in C:
            nums.add(a + b + c)
print(*["Yes" if x in nums else "No" for x in X], sep="\n")
