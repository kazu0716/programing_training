A, B, C = map(int, input().split())

if (A == B and B != C) or (B == C and B != A) or (A == C and B != C):
    print("Yes")
else:
    print("No")
