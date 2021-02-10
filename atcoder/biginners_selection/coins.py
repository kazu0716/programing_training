A = int(input()) + 1
B = int(input()) + 1
C = int(input()) + 1
X = int(input())

print(len([(a, b, c) for a in range(A) for b in range(B)
           for c in range(C) if 500 * a + 100 * b + 50 * c == X]))
