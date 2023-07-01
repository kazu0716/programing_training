def is_no(n):
    if not (100 <= n <= 675):
        exit(print("No"))
    if n % 25 != 0:
        exit(print("No"))


S = tuple(map(int, input().split()))
for i in range(len(S) - 1):
    if S[i] > S[i + 1]:
        exit(print("No"))
    is_no(S[i])
is_no(S[-1])
print("Yes")
