from sys import exit

N = int(input())
A = list(map(int, input().split()))
s = sum(A)
if s % 10 != 0:
    print("No")
    exit()
r, length = 0, 0
for l in range(N):
    while length < s//10:
        length += A[r % N]
        r += 1
    if length == s//10:
        print("Yes")
        exit()
    length -= A[l]
print("No")
