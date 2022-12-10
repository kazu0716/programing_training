from re import match

S = input()
print("Yes" if match(r"[A-Z][1-9][0-9]{5}[A-Z]", S) else "No")
