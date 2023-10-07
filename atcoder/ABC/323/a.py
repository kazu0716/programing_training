S = input()
print("Yes" if int(S, 2) & int("01" * 8, 2) == 0 else "No")
