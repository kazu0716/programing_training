N = int(input())
S = sum([int(s) for s in str(N)])
print("Yes" if N % S == 0 else "No")
