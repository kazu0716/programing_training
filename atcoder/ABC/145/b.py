N = int(input())
S = input()

if N % 2 != 0:
    print("No")
else:
    n = len(S)//2
    if S[0:n] == S[n:]:
        print("Yes")
    else:
        print("No")
