_ = int(input())
S = input()
print("Yes" if (S[0] == "B" or S[-1] == "A") and S != "BA" else "No")
