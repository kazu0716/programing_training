S = input()
if S[0] == "<" and S[-1] == ">" and len(set(S[1:-1])) == 1 and S[1] == "=":
    exit(print("Yes"))
print("No")
