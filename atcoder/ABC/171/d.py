N = int(input())
A = list(map(int, input().split()))
Q = int(input())

s = sum(A)
nums = {}
ans = []

for i in range(len(A)):
    a = A[i]
    if a in nums:
        nums[a] += 1
    else:
        nums[a] = 1

for _ in range(Q):
    B, C = map(int, input().split())
    if B not in nums:
        ans.append(s)
        continue
    s += (C - B) * nums[B]
    if C in nums:
        nums[C] += nums[B]
    else:
        nums[C] = nums[B]
    del nums[B]
    ans.append(s)
print(*ans, sep="\n")
