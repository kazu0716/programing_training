import sys

A, B = map(str, input().split())
A, B = list(A), list(B)

for _ in range(min(len(A), len(B))):
    a, b = int(A.pop()), int(B.pop())
    if a + b >= 10:
        print("Hard")
        sys.exit()

print("Easy")
